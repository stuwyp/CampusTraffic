


window.onload = function(){

    //图片动画
     var Obque = new Array();
    var moveObj = document.getElementById("image");
    var img = moveObj.getElementsByTagName("img");


    for(var i = 0;i < img.length;i++){
        Obque.push(img[i]);
    }

    setInterval(function(){
    img_move(Obque);},3000);

    }




function img_move(Obque){

    //图片动画

    var obj0 = Obque.shift();

    obj0.style["z-index"] = 0;
    startMove(obj0,{"left":200,"opacity":0});

    var obj1 = Obque.shift();
    startMove(obj1,{"left":0,"opacity":50});
    obj1.style["z-index"] = 0;
    Obque.push(obj1);

    var obj2 = Obque.shift();
    startMove(obj2,{"left":200,"opacity":100});
    obj2.style["z-index"] = 1;
    Obque.push(obj2);


    var obj3 = Obque.shift();
    startMove(obj3,{"left":450,"opacity":50});
    obj3.style["z-index"] = 0;
    Obque.push(obj3);
    Obque.push(obj0);


}


