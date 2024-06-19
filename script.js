var images = {
    'Длинные волосы' : [
        'pic7.jpg',
        'pic3.jpg',
        'pic5.jpg',
        'pic13.jpg',
        'pic14.jpg',
        'pic8.jpg',
        'pic15.jpg',
        'pic16.jpg',
        'pic17.jpg',
        'pic9.jpg'
    ],
    'Средние волосы' : [
        'pic2.jpg',
        'pic6.jpg',
        'pic10.jpg',
        'pic1.jpg',
        'pic11.jpg',
        'pic12.jpg',
        'pic18.jpg',
        'pic19.jpg',
        'pic20.jpg',
        'pic21.jpg'
    ],
    'Короткие волосы' : [
        'pic4.jpg',
        'pic22.jpg',
        'pic23.jpg',
        'pic24.jpg',
        'pic25.jpg',
        'pic26.jpg',
        'pic27.jpg',
        'pic28.jpg',
        'pic29.jpg',
        'pic30.jpg'
    ]
};
$(document).ready(function(){ 
    $('#gallery').gallery();
});


$.fn.gallery = function() {
var rself = this;
var setimgs;

this.each(function() {
var g = this;

g.load_sets = function(el) {
            $.each(images, function(key, value) { 
                $(el).append('<li><a id="'+key+'" href="#bloc_5" title="'+key+'">'+key+'</a></li>');
            });
var sets = $(el).find('li a');
            $(sets).click(function() { 
var set = $(this).attr('id');
g.setimgs = images[set];
                $(g).find('#thumbs').html('');
g.load_thumbs($(g).find('#thumbs')[0], 0);

                $(g).find('#loading').html('Загрузка <strong>1</strong> из '+g.setimgs.length+' изображений');
            });
sets[0].click();
        }
g.load_thumbs = function(el, index) { 
            $(el).append('<li><img id="' + g.setimgs[index] + '" src="images/thumb_' + g.setimgs[index] + '" /></li>');
var tn = new Image();
$(tn).load(function() {
var a = $($(el).find('li')[index]).find('img')[0];
                $(a).append(this);
                $(a).click(function() { 
var i = $(this).attr('id');
                    $(g).find('#photo').attr('src', 'images/'+i);
return false;
                });
if ((index + 1) <g.setimgs.length) {
g.load_thumbs(el, (index + 1));
                    $(g).find('#loading strong').html(index + 2);
                } else {
                    $(g).find('#loading').html('Загружено изображений: <strong>' + g.setimgs.length + '</strong>');
                    $($(g).find('#thumbs li img')[0]).click();
                }
            });
tn.src = 'images/thumb_' + g.setimgs[index];
}

g.load_sets($(g).find('#sets')[0]);
    });
};

