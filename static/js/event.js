$("document").ready( function() {
    
    addEventItem();

    //$('#datetimepicker').datetimepicker();

});

$("#create_button").click(
    function(){
        var event_data = {};

        event_data.name = $("#event_name_input").val();
        event_data.description =  $("#event_description_input").val();
        event_data.email =  $("#event_email_input").val();
        event_data.items= [];

        $("#event_items div").each(function() {
          var ei = {};
          ei.category = $(".item_category",this).val();
          ei.time = $(".item_time",this).val();
          event_data.items.push(ei);
        });

        console.log(event_data);

        create_event(JSON.stringify(event_data));
    }
);

$("#add_event_item").click(
  function() {
    addEventItem();
  }
);

function addEventItem()
{
  var event_item = $("<div>");
  
  item_category = $("<input/>", {
                        type: 'text',
                        class: 'item_category'
                    });

  item_time = $("<input/>", {
                        type: 'text',
                        class: 'item_time'
                    });

  item_time.datetimepicker({
    format:'d.m.Y H:i'
  }); //http://xdsoft.net/jqplugins/datetimepicker/

  event_item.append(item_category,item_time);
  $("#event_items").append(event_item);
}

function create_event(event_data) {
  $.ajax({
    url: "/create_event/",
    type: "POST",
    data: event_data,
    cache: true,
    success: function (data, textStatus, jqXHR) {
      if(data.success)
          {
            $("#info").text("Created new event!");
            window.location.replace("http://localhost:8000/event/"+data.id);
          }
          else
          {
            $("#info").text("Something wrong with creating new event!");
          }
      
    },
    complete: function (jqXHR, textStatus) {},
    error: function (data, textStatus, errorThrown) {
      $("#info").text("Error with event creation!");
    }
  });

}
