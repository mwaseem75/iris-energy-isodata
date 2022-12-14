/// Description
Class Grongier.PEX.Test Extends %Persistent
{

/// Register
ClassMethod Register() As %Status
{
	Set sc = $$$OK
	zw ##class(Grongier.PEX.Utils).RegisterComponent("MyBusinessOperationWithAdapter","MyBusinessOperationWithAdapter","/irisdev/app/src/python/demo/",1,"PEX.MyBusinessOperationWithAdapter")
	#dim array as %ArrayOfObjects
	Return sc
}

ClassMethod TestBO() As %Status
{
	try {
	Set sc = $$$OK
	set mybo = ##class(Grongier.PEX.BusinessOperation).%New("mybo")
	set mybo.%classpaths = "/irisdev/app/src/python/demo"
	set mybo.%module = "MyBusinessOperationWithAdapter"
	set mybo.%classname = "MyBusinessOperationWithAdapter"
	$$$ThrowOnError(mybo.OnInit())
	set request = ##class(Ens.StringRequest).%New("hello")
	set request = ##class(EnsLib.PEX.Message).%New()
	set request.%classname = "MyRequest.MyRequest"
	set dyna = {"requestString":"hello!"}
	set request.%jsonObject = dyna
	Try {
		$$$ThrowOnError(mybo.OnMessage(request,.response))
		zw response
	} catch importEx {
		WRITE $System.Status.GetOneStatusText(importEx.AsStatus(),1),!
	}
	} catch ex {
		WRITE $System.Status.GetOneStatusText(ex.AsStatus(),1),!
	}

	Return sc
}

/// List
ClassMethod PythonList() [ Language = python ]
{
return [ 1, 3 ]
}

Storage Default
{
<Data name="TestDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
</Data>
<DataLocation>^Grongier.PEX.TestD</DataLocation>
<DefaultData>TestDefaultData</DefaultData>
<IdLocation>^Grongier.PEX.TestD</IdLocation>
<IndexLocation>^Grongier.PEX.TestI</IndexLocation>
<StreamLocation>^Grongier.PEX.TestS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
