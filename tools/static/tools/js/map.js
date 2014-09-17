ymaps.ready(init);
    var myMap;
    var myPlacemark;

function init(){     
    myMap = new ymaps.Map("map", {
        center: [59.894034,30.412095],
        zoom: 15,
    });
    
    myPlacemark = new ymaps.Placemark([59.892775,30.407578], { 
        hintContent: 'Санкт-Петербург, пр.Елизарова, д.34, к.2, литера Б', 
        balloonContentHeader: 'Центр профессиональной заточки TOGU',
        balloonContentBody: 'Санкт-Петербург, пр.Елизарова, д.34, к.2, литера Б',
        iconContent: 'Мы находимся здесь', 
    }, {
        preset: 'islands#lightBlueStretchyIcon'
    }) ;
    
    myMap.geoObjects.add(myPlacemark);
    myMap.controls.add('routeEditor');
    myMap.controls.add('zoomControl');
}