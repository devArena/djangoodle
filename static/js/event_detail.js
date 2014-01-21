$("#add_participant").click(function() {
    var selected_items = $.map($("#event_item_list input:checked"),function(t){return t.id;});
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
          $("#info_add_participant").text("Added new participant!");
          render_participant(data);
        },
        complete: function (jqXHR, textStatus) {},
        error: function (data, textStatus, errorThrown) {
          $("#info_add_participant").text("Error with adding new participant!");
        }
    });

  });

function render_participant(participant_data)
{


}