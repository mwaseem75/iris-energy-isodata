Class PEX.Production Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="PEX.Production" TestingEnabled="true" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  
  <Item Name="Isodata.CaliforniaService" Category="" ClassName="Python.CaliforniaService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%settings">limit=10</Setting>
  </Item>
  
  <Item Name="Isodata.TexasService" Category="" ClassName="Python.TexasService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%settings">limit=10</Setting>
  </Item>

  <Item Name="Isodata.NewYorkService" Category="" ClassName="Python.NewYorkService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%settings">limit=10</Setting>
  </Item>

  <Item Name="Isodata.SouthWestService" Category="" ClassName="Python.SouthWestService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%settings">limit=10</Setting>
  </Item>

  <Item Name="Isodata.PjmService" Category="" ClassName="Python.PjmService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%settings">limit=10</Setting>
  </Item>

  <Item Name="Isodata.MidcontinentService" Category="" ClassName="Python.MidcontinentService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%settings">limit=10</Setting>
  </Item>

  <Item Name="Isodata.Isone" Category="" ClassName="Python.IsoneService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%settings">limit=10</Setting>
  </Item>

  <Item Name="Isodata.FilterRoutingRule" Category="" ClassName="Python.FilterPostRoutingRule" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>

  <Item Name="Isodata.CaliforniaOperation" Category="" ClassName="Python.FileOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/irisdev/app/output/</Setting>
    <Setting Target="Host" Name="%settings">path=/irisdev/app/output/</Setting>
  </Item>

  <Item Name="Isodata.TexasOperation" Category="" ClassName="Python.FileOperation" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/irisdev/app/output/</Setting>
    <Setting Target="Host" Name="%settings">path=/irisdev/app/output/</Setting>
  </Item>

  <Item Name="Isodata.NewYorkOperation" Category="" ClassName="Python.FileOperation" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/irisdev/app/output/</Setting>
    <Setting Target="Host" Name="%settings">path=/irisdev/app/output/</Setting>
  </Item>

  <Item Name="Isodata.SouthWestOperation" Category="" ClassName="Python.FileOperation" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/irisdev/app/output/</Setting>
    <Setting Target="Host" Name="%settings">path=/irisdev/app/output/</Setting>
  </Item>

 <Item Name="Isodata.PjmOperation" Category="" ClassName="Python.FileOperation" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/irisdev/app/output/</Setting>
    <Setting Target="Host" Name="%settings">path=/irisdev/app/output/</Setting>
  </Item>

<Item Name="Isodata.MidcontinentOperation" Category="" ClassName="Python.FileOperation" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/irisdev/app/output/</Setting>
    <Setting Target="Host" Name="%settings">path=/irisdev/app/output/</Setting>
  </Item>

<Item Name="Isodata.IsoneOperation" Category="" ClassName="Python.FileOperation" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/irisdev/app/output/</Setting>
    <Setting Target="Host" Name="%settings">path=/irisdev/app/output/</Setting>
  </Item>

</Production>
}

}
