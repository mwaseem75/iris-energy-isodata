/* Copyright (c) 2021 by InterSystems Corporation.
   Cambridge, Massachusetts, U.S.A.  All rights reserved.
   Confidential property of InterSystems Corporation. */

Class Grongier.PEX.InboundAdapter Extends (Ens.InboundAdapter, Grongier.PEX.Common) [ Inheritance = right, ProcedureBlock, System = 4 ]
{

Parameter SETTINGS = "%classname:Python InboundAdapter,%module:Python InboundAdapter,%settings:Python InboundAdapter,%classpaths:Python InboundAdapter";

/// Use Host Connection. If set to true, this adapter will use the connection from the host.
Property %useHostConnection As %Boolean [ Internal ];

Method OnTask() As %Status
{
	set tSC = $$$OK
	try {
		set tSC = ..Connect() quit:$$$ISERR(tSC)
		do ..%class.OnTask()
	} catch ex {
		set tSC = ex.AsStatus()
	}
	quit tSC
}

}