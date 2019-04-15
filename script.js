function fetchNewData(query, targetElementId, doAfter){
    var targetElement = document.getElementById(targetElementId);
    fetch(query)
    .then(
      function(response){
        return response.text();
      })
      .then(function(text){
          targetElement.innerHTML = text;
          doAfter();
          })
    }
  
  function addEventListenerToTables(){
    var dbtable = document.getElementById("dbtable");
    dbtable.addEventListener('change', updateWholeTableView)
    }
  
  function doNothing(){
    }
  
  function updateWholeTableView(){
    var selected_table = document.getElementById("dbtable").value
    fetchNewData('./cgi-bin/runsql.py?table=' + selected_table,"output_table", doNothing);
    }
  
  function displayQueryResult(){
    var sqlquery = document.getElementById("sqlquery").value
    sqlquery = sqlquery.replace(/\n/g," ");
    fetchNewData('./cgi-bin/runsql.py?sql=' + sqlquery,"output_table", doNothing);
    }
  
  function insertTableMenu(){
    fetchNewData('./cgi-bin/listtables.py', "dbtables_div", addEventListenerToTables);
    }
