var map = new BMap.Map("container");          // 创建地图实例


    map.centerAndZoom(new BMap.Point(116.639956, 23.420278),18);

	map.addControl(new BMap.MapTypeControl());   //添加地图类型控件

	var b = new BMap.Bounds(new BMap.Point(116.634171, 23.415075),
	new BMap.Point(116.646676, 23.427344));

	var mapStyle={  style : "grassgreen" };
    map.setMapStyle(mapStyle);

    var driving = new BMap.DrivingRoute(map, {
    renderOptions: {
        map   : map,
        panel : "results",
        autoViewport: true
    }
});





    var car_start = new BMap.Point(116.644471,23.414607);

    var position = [116.642892,23.419723,
                    116.642191,23.419254,
                    116.642034,23.41821,
                    116.641558,23.416705,
                    116.639595,23.416357,
                    116.635768,23.416527,
                    116.640161,23.420929,
                    116.63928,23.420046,
                    116.636464,23.42102,
                    116.639483,23.416726,
                    116.643543,23.417919,


                    ];

     // 创建标注
    for(var i = 0;i<position.length;i+=2) {
    var marker = new BMap.Marker(new BMap.Point(position[i],position[i+1]));
    map.addOverlay(marker);


    }

    map.addEventListener("click", function(e){
    driving.search(car_start,new BMap.Point(e.point.lng,e.point.lat));  //点击显示驾车路线
});











