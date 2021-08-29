/* Copyright (c) 2021 by InterSystems Corporation.
   Cambridge, Massachusetts, U.S.A.  All rights reserved.
   Confidential property of InterSystems Corporation. */

Include Ensemble

Class Grongier.PEX.Common [ Abstract, ClassType = "", ProcedureBlock, System = 4 ]
{

/// One or more Classpaths (separated by '|' character) needed in addition to the ones configured in the Java Gateway Service
Property %classpaths As %String(MAXLEN = "");

Property %classname As %String(MAXLEN = "") [ Internal ];

Property %module As %String(MAXLEN = "") [ Internal ];

Property %settings As %String(MAXLEN = "") [ Internal ];

/// Instance of class
Property %class As %SYS.Python;

Method OnInit() As %Status
{
	set tSC = $$$OK
	try {
        $$$ThrowOnError(..Connect())
		do ..%class."_dispatchOnInit"($this)
	} catch ex {
		set tSC = ex.AsStatus()
	}
	quit tSC
}

Method Connect() As %Status
{
	set tSC = $$$OK
	try {
		
		if ..%Extends("Grongier.PEX.InboundAdapter") || ..%Extends("Grongier.PEX.OutboundAdapter") {
			set container = $s(..%useHostConnection:..BusinessHost,1:$this)
		} else {
			set container = $this
		}
		;
		if container'=$this set ..%class = container.%class
		;
		//set classpass
		if ..%classpaths '="" {
			set delimiter = $s($system.Version.GetOS()="Windows":";",1:":")
			set extraClasspaths = $tr(container.%classpaths,delimiter,"|")
			for i=1:1:$l(extraClasspaths,"|") {
				set onePath = $p(extraClasspaths,"|",i)
				if onePath?1"$$IRISHOME"1P.E set onePath = $e($system.Util.InstallDirectory(),1,*-1)_$e(onePath,11,*)
				if onePath'="" do ##class(Grongier.PEX.Common).SetClassPath(onePath)
			}
		}
		;
		
		if $isObject(..%class)=0 {
			set ..%class = ##class(Grongier.PEX.Common).GetInstanceFromModuleClassName(..%module,..%classname)
		}
		;
		if ..%Extends("EnsLib.PEX.InboundAdapter") || ..%Extends("EnsLib.PEX.OutboundAdapter") {
			do ..%class."_setIrisHandles"($this,..BusinessHost)
		} elseif $this.%Extends("EnsLib.PEX.BusinessProcess") {
			do ..%class."_setIrisHandles"($this,$$$NULLOREF)
		} else {
			do ..%class."_setIrisHandles"($this,..Adapter)
		}
		;
		do ..SetPropertyValues()
		;
		try {
			do ..%class."_dispatchOnConnected"($this)
		} catch ex {
			$$$LOGWARNING(ex.DisplayString())
		}
		;
	} catch ex {
		set msg = $System.Status.GetOneStatusText(ex.AsStatus(),1)
		set tSC = $$$ERROR($$$EnsErrGeneral,msg)
	}
	quit tSC
}

Method OnTearDown() As %Status
{
	set tSC = $$$OK
    do ..%class.OnTearDown()
	quit tSC
}

Method SetPropertyValues()
{
	set remoteSettings = $tr(..%settings,$c(13))
	for i=1:1:$l(remoteSettings,$c(10)) {
		set oneLine = $p(remoteSettings,$c(10),i)
		set property = $p(oneLine,"=",1) continue:property=""
		set value = $p(oneLine,"=",2,*)
		try {
			set $property(..%class,property) = value
		} catch ex {
			$$$LOGWARNING(ex.DisplayString())
		}
	}
	quit
}

Method dispatchSendRequestSync(target, request, timeout, description) As %String
{
	if request'="",$isObject(request)=0 set request = ..deserialize(request)
	set tSC = ..SendRequestSync(target,request,.objResponse,timeout,description)
	if $$$ISERR(tSC) throw ##class(%Exception.StatusException).CreateFromStatus(tSC)
	if $isObject($g(objResponse)),objResponse.%IsA("EnsLib.PEX.Message") set objResponse = ..serialize(objResponse)
	quit $g(objResponse)
}

Method dispatchSendRequestAsync(target, request, description)
{
	if request'="",$isObject(request)=0 set request = ..deserialize(request)
	set tSC = ..SendRequestAsync(target,request,description)
	if $$$ISERR(tSC) throw ##class(%Exception.StatusException).CreateFromStatus(tSC)
	quit
}

ClassMethod serialize(message As EnsLib.PEX.Message) As %String
{
	if $g(message)=$$$NULLOREF quit ""
	quit message.%classname_":"_message.%jsonObject.%ToJSON()
}

ClassMethod deserialize(serialized As %String = "") As EnsLib.PEX.Message
{
	if serialized = "" {
		set message = $$$NULLOREF
	} else {
		set message = ##class(EnsLib.PEX.Message).%New()
		set message.%classname = $p(serialized,":",1)
		set json = $p(serialized,":",2,*)
		if json="" set json = "{}"
		set message.%jsonObject = ##class(%DynamicObject).%FromJSON(json)
	}
	quit message
}

/// Set classPath
ClassMethod SetClassPath(classPath As %String) As %Status [ Language = python ]
{
import sys
return sys.path.append(classPath)
}

/// GetInstanceFromModuleClassName
ClassMethod GetInstanceFromModuleClassName(modulename, classname) As %SYS.Python [ Language = python ]
{
import builtins
module = __import__(modulename)
return getattr(module, classname)()
}

/// Lenght of python list
ClassMethod Len(pList) [ Language = python ]
{
return len(pList)
}

}