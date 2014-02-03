$( document ).ready(function() {
    
     refresh_table();
});

$("#add_participant").click(function() {
    var selected_items = $.map($("#new_participant input:checked"),function(t){return t.id;});
    var participant_name = $("#participant_name").val();

    var participant_data = {};
    participant_data.selected_items = selected_items;
    participant_data.participant_name = participant_name;
    participant_data.event_id = event_id;
    console.log(participant_data);

    $.ajax({
        url: "/add_participant/",
        type: "POST",
        data: JSON.stringify(participant_data),
        cache: true,
        success: function (data, textStatus, jqXHR) {
          if(data.success)
          {
            $("#info_add_participant").text("Added new participant!");
            reset_participant_input();
            render_participant(data);
            refresh_stats();
          }
          else
          {
            $("#info_add_participant").text("Something wrong with adding new participant!");
          }
        },
        complete: function (jqXHR, textStatus) {},
        error: function (data, textStatus, errorThrown) {
          $("#info_add_participant").text("Error with adding new participant!");
        }
    });

  });

$("#refresh_table").click(function(){
    refresh_table()
});

function refresh_table()
{
  //+console.log("refresh");
  $.ajax({
      url:"/get_participants/" + event_id + "/",
      type:"GET",
      cache:true,
      success: function(data, textStatus, jqXHR){
        //console.log(data);
        if(data.success)
        {
          reset_table();  
          for(var i=0; i<data.participants.length; i++)
          {
            render_participant(data.participants[i]);
          }
          $("#info_add_participant").text("Table refreshed!"); 
          refresh_stats();         
        }
        else
        {
          $("#info_add_participant").text("Something wrong with refreshing");
        }              
      },
      complete: function(jqXHR, textStatus){},
      error: function(data, textStatus, errorThrown){
        $("#info_add_participant").text("Error with refreshing table");
      }
  });    
}

function reset_table()
{
  //remove <tr> that represent participants
  $('tr[id^=participant]').remove();
}

function reset_participant_input()
{
  $("#participant_name").val("");
  $("#new_participant input:checked").attr('checked', false);
}

function render_participant(participant_data){
  var par = $('<tr>');
  par.attr('id', 'participant_'+participant_data.participant_id);
  par.append($('<td><p>'+ participant_data.participant_name 
                        + ' <span id="edit_id_' + participant_data.participant_id + '" class="glyphicon glyphicon-pencil"></span> '
                        + ' <span id="delete_id_' + participant_data.participant_id + '" class="glyphicon glyphicon-trash"></span> '
                        + ' </p></td>'));

  var j = 0;
  sel_items = participant_data.selected_items;
  for(var i=0;i<event_items_id.length;i++)
  {
    var td = $('<td>');
    td.attr('id', event_items_id[i]);
    if(j < sel_items.length && event_items_id[i] === +sel_items[j])
    {
      td.append('<img src="http://www.packvol.com/img/checked.gif"/>');
      td.addClass('selected');
      j++;
    }
    else
    {
      td.append('<img src="http://www.packvol.com/img/unchecked.gif"/>');
      td.addClass('not-selected');
    }
    par.append(td);
  }

  $('#new_participant').before(par);

  $('#delete_id_'+participant_data.participant_id).click(function(){delete_participant(participant_data.participant_id);});
  $('#edit_id_'+participant_data.participant_id).click(function(){edit_participant(participant_data);});

}

function refresh_stats(){

  for(var i=0;i<event_items_id.length;i++)
  {
    var id = event_items_id[i];
    var num_of_sel = $('td.selected[id='+ id +']').length;
    $('#stat_' +id).text(num_of_sel);
  }

}

function delete_participant(participant_id) {

    // console.log(participant_id);

    $.ajax({
        url: "/delete_participant/",
        type: "POST",
        data: JSON.stringify({'participant_id':participant_id}),
        cache: true,
        success: function (data, textStatus, jqXHR) {
          if(data.success)
          {
            refresh_table();
          }
          else
          {
            // $("#info_add_participant").text("Something wrong with adding new participant!");
          }
        },
        complete: function (jqXHR, textStatus) {},
        error: function (data, textStatus, errorThrown) {
          // $("#info_add_participant").text("Error with adding new participant!");
        }
    });

  }

function edit_participant(participant_data) {

    var par_id = participant_data.id;
    var par_name = participant_data.participant_name;
    var sel_items = participant_data.selected_items;
    
    console.log(participant_data);
    
    var tr_par = $('#participant_' + par_id);    
    
    label_par_name = $('<label>Name:</label>')
    input_par_name = $('<input type="text">' + par_name + '<input/>');   
    var td_par = $('<td>');
    td_par.append(label_par_name, input_par_name);

    var j = 0;
    for(var i=0;i<event_items_id.length;i++)
    {
      var td = $('<td>');
      td.attr('id', event_items_id[i]);
      var chbx = $('<input type="checkbox" id="edit_' + event_items_id[i] + '">');
      if(j < sel_items.length && event_items_id[i] === +sel_items[j])
      {   
        j++;
      }
      else
      {
        td.append('<img src="http://www.packvol.com/img/unchecked.gif"/>');
        td.addClass('not-selected');
      }
      td.append(chbx);
      par.append(td);
    }

    tr_par.empty();
    tr_par.append(td_par);


    // $.ajax({
    //     url: "/edit_participant/",
    //     type: "POST",
    //     data: JSON.stringify({'participant_id':participant_id}),
    //     cache: true,
    //     success: function (data, textStatus, jqXHR) {
    //       if(data.success)
    //       {
    //         refresh_table();
    //       }
    //       else
    //       {
    //         // $("#info_add_participant").text("Something wrong with adding new participant!");
    //       }
    //     },
    //     complete: function (jqXHR, textStatus) {},
    //     error: function (data, textStatus, errorThrown) {
    //       // $("#info_add_participant").text("Error with adding new participant!");
    //     }
    // });

  }