jQuery(function($) {

	var $window = $(window);
	var $body = $('body');
	var $header = $('#header');
	$window.on('scroll', function(e) {
		var scrollTop = $window.scrollTop();
		$header.toggleClass('minimal', scrollTop > 0);
		$body.toggleClass('minimal-header', scrollTop > 0);
	});

  $('body').addClass('postload');

	$(document).ready(function() {

      $(".hamburger").click(function(){
        $("body").toggleClass("menu-open");
      });

    // Add fullwidth class to gallery thumbs if less than 6
    	
    $('.imageGallery').each(function(){
      if ($(this).children('div').length <= 6) {
        $(this).children('div').addClass('fullwidth-mobile');
      }
    });

    // Watch for changes on non-mobile nav

    var mainNav = '#nav',
        mobileNav = "#navmobile";

    $(mainNav).on('DOMSubtreeModified propertychange', function() {
      if ($(window).width() < 768) {
        $(mainNav + " li a").each(function(){
          // Differentiating post-load nav elements by the presence of an id
          if ($(this).attr("id")) {
            var navLinkId = $(this).attr("id");
            var navLinkParent = $(this).parent().detach();

            // Append to mobile nav if new element
            if (!$(mobileNav + " #"+navLinkId).length) {
              $(mobileNav + " .wsite-menu-default").append(navLinkParent);
              var newheight = $(mobileNav + " .wsite-menu-default").height();
              $(".wsite-mobile-menu").height(newheight);
            }
          }
        });
      }
    });

    $(window).resize(function() {
      var newheight = $(mobileNav + " .wsite-menu-default").height();
      $(".wsite-mobile-menu").height(newheight);
    });

    // Add swipe to fancybox mobile 

    var swipeGallery = function(){
      setTimeout(function(){
      var touchGallery = document.getElementsByClassName("fancybox-wrap")[0];
      var mc = new Hammer(touchGallery);
      mc.on("panleft panright", function(ev) {
        if (ev.type == "panleft") {
          $("a.fancybox-next").trigger("click");
        }
        else if (ev.type == "panright") {
          $("a.fancybox-prev").trigger("click");
        }
        swipeGallery();
      });
      }, 500);
    }
    if ($(window).width() < 1024) {
      $("body").on( "click", "a.w-fancybox", function() {
        swipeGallery();
      });
    }

  });


});