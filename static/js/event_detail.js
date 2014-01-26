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
  //console.log("refresh");
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

function render_participant(participant_data)
{
  var par = $('<tr>');
  par.attr('id', 'participant_'+participant_data.participant_id);
  par.append($('<td><p>'+ participant_data.participant_name +'</p></td>'));

  var j = 0;
  sel_items = participant_data.selected_items;
  for(var i=0;i<event_items_id.length;i++)
  {
    if(j < sel_items.length && event_items_id[i] === +sel_items[j])
    {
      par.append('<td><img src="http://www.packvol.com/img/checked.gif"/></td>');
      j++;
    }
    else
    {
      par.append('<td><img src="http://www.packvol.com/img/unchecked.gif"/></td>');
    }
  }

  $('#new_participant').before(par);
}
