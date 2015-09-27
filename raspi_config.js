var raspi_locs = [];
$(document).ready(function(){
    $("img").click(function(e) {
        var offset = $(this).offset();
        raspi_locs.push([(e.pageX - offset.left),(e.pageY - offset.top)]); //RASPILOCS STORES COORDS RELATIVE TO IMAGE. Do not resize page after this.
        
        //Draw marker on map
        var d = document.createElement("div");
        d.className = "rp";
        d.id = "marker"+raspi_locs.length;
        document.body.appendChild(d);
        m = document.getElementById("marker"+raspi_locs.length);
        m.style.left=raspi_locs[raspi_locs.length-1][0]+offset.left-m.offsetWidth/2+"px";
        m.style.top=raspi_locs[raspi_locs.length-1][1]+offset.top-m.offsetHeight/2+"px";
        
        //Post location to server
        var jsonobj = {
                "raspi_id": raspi_locs.length,
                "x": raspi_locs[raspi_locs.length-1][0],
                "y": raspi_locs[raspi_locs.length-1][1]
        };

        var form = document.createElement("form");
        form.setAttribute("method","post");
        form.setAttribute("action","/raspiCoord/");

        for(var key in jsonobj) {
            if(jsonobj.hasOwnProperty(key)) {
                var hiddenField = document.createElement("input");
                hiddenField.setAttribute("type","hidden");
                hiddenField.setAttribute("name",key);
                hiddenField.setAttribute("value",jsonobj[key]);

                form.appendChild(hiddenField);
            }
        }

        document.body.appendChild(form);
        form.submit();
    });
});
