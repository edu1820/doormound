(function($){
	
	$(document).ready(function(){
		var slides = $("#slideshow > li");
		var count = 0;

		function slide_show (){
			count = (count + 1) % 3;
			slides.removeClass ("current").eq(count).addClass("current");
		}
		setInterval (slide_show ,2000);
	});

})(jQuery);