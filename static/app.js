$(function(){

    var dragHandler = function(evt){
        evt.preventDefault();
    };

    var dropHandler = function(evt){
        evt.preventDefault();
        var files = evt.originalEvent.dataTransfer.files;

        var formData = new FormData();
        formData.append("inputFile", files[0]);

        var req = {
            url: "/upload",
            method: "post",
            processData: false,
            contentType: false,
            data: formData,
            // reloads view to update results
            success: function(result) {
                location.reload(true);
            }
        };

        $.ajax(req);
    };

    var dropHandlerSet = {
        dragover: dragHandler,
        drop: dropHandler
    };
    $(".droparea").on(dropHandlerSet);
});
