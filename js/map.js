//get list of clusters from server
var pts = httpGetFormatted("/positions/");

var clusters_r = [[2],[1]];
*/
//render points/clusters
for(var key in pts) {
    if(pts.hasOwnProperty(key)) {
        renderNew(key,pts[key].pos_x,pts[key].pos_y);
    }
}

function httpGetFormatted(url) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET",url,false);
    xmlHttp.send(null);
    var json_in = JSON.parse(xmlHttp.responseText);
    var as_arr = {};
    for(var i=0;i<json_in.length;i++){
        as_arr[json_in[i].mac] = json_in[i];
    }
    return as_arr;
}

function renderNew(idnum,x,y) {
    var d = document.createElement("div");
    d.className="pt";
    d.id="d"+idnum;
    document.body.appendChild(d);
    document.getElementById("d"+idnum).style.left=x+"px";
    document.getElementById("d"+idnum).style.top=y+"px";
}

function updateData() {
    var pts_new = httpGetFormatted("/positions");
    for(var key in pts_new) {
        //rerender dkey if it didn't appear in the previous frame
        if(!pts[key]) { 
            renderNew(key,pts_new[key].pos_x,pts_new[key].pos_y);
        } else { 
            document.getElementById("d"+key).style.left=pos_x+"px";
            document.getElementById("d"+key).style.left=pos_y+"px";
        }
    }

    setTimeout(updateData(),1000)
    pts = pts_new;
}


//button to switch between cluster and point view, or switch on zoom 