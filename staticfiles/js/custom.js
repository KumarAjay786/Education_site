/******************************************
    File Name: custom.js
*******************************************/

"use strict";

/**== WOW animation ==**/
new WOW().init();

/**== Loader JS ==**/
$(window).on('load', function() {
    $(".bg_load").fadeOut("slow");
});

/**== Menu JS ==**/
$("#navbar_menu").menumaker({
    title: "Menu",
    format: "multitoggle"
});

/**== Counter JS ==**/
$('.counter-count').each(function () {
    $(this).prop('Counter', 0).animate({
        Counter: $(this).text()
    }, {
        duration: 5000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
});

/**== Progress Bar JS ==**/
$(document).ready(function() {
    $('.progress .progress-bar').css("width", function() {
        return $(this).attr("aria-valuenow") + "%";
    });
});

/**== Case Studies Tab Filter JS ==**/
$(document).ready(function(){
    $(".filter-button").click(function(){
        var value = $(this).attr('data-filter');

        if (value === "all") {
            $('.filter').show('1000');
        } else {
            $(".filter").not('.' + value).hide('3000');
            $('.filter').filter('.' + value).show('3000');
        }
    });

    $(".filter-button").removeClass("active");
    $(this).addClass("active");
});

/**== Google Map Function (requires Google Maps API) ==**/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

/**== Revolution Slider Initialization ==**/
var tpj = jQuery;
var revapi4;

tpj(document).ready(function() {
    if (tpj("#rev_slider_4_1").revolution === undefined) {
        // Prevent crashing if the function is not defined
        if (typeof revslider_showDoubleJqueryError === "function") {
            revslider_showDoubleJqueryError("#rev_slider_4_1");
        } else {
            console.error("Revolution Slider is not loaded properly. Check JS file paths.");
        }
    } else {
        revapi4 = tpj("#rev_slider_4_1").show().revolution({
            sliderType: "standard",
            jsFileLocation: "/static/revolution/js/",
            sliderLayout: "fullwidth",
            dottedOverlay: "none",
            delay: 7000,
            navigation: {
                keyboardNavigation: "off",
                keyboard_direction: "horizontal",
                mouseScrollNavigation: "off",
                onHoverStop: "off",
                touch: {
                    touchenabled: "on",
                    swipe_threshold: 75,
                    swipe_min_touches: 1,
                    swipe_direction: "horizontal",
                    drag_block_vertical: false
                },
                arrows: {
                    style: "zeus",
                    enable: true,
                    hide_onmobile: true,
                    hide_under: 600,
                    hide_onleave: true,
                    hide_delay: 200,
                    hide_delay_mobile: 1200,
                    tmp: '<div class="tp-title-wrap"><div class="tp-arr-imgholder"></div></div>',
                    left: {
                        h_align: "left",
                        v_align: "center",
                        h_offset: 30,
                        v_offset: 0
                    },
                    right: {
                        h_align: "right",
                        v_align: "center",
                        h_offset: 30,
                        v_offset: 0
                    }
                },
                bullets: {
                    enable: true,
                    hide_onmobile: true,
                    hide_under: 600,
                    style: "metis",
                    hide_onleave: true,
                    hide_delay: 200,
                    hide_delay_mobile: 1200,
                    direction: "horizontal",
                    h_align: "center",
                    v_align: "bottom",
                    h_offset: 0,
                    v_offset: 30,
                    space: 5,
                    tmp: '<span class="tp-bullet-img-wrap">  <span class="tp-bullet-image"></span></span><span class="tp-bullet-title">{{title}}</span>'
                }
            },
            viewPort: {
                enable: true,
                outof: "pause",
                visible_area: "80%"
            },
            responsiveLevels: [1240, 1024, 778, 480],
            gridwidth: [1240, 1024, 778, 480],
            gridheight: [700, 700, 500, 400],
            lazyType: "none",
            parallax: {
                type: "mouse",
                origo: "slidercenter",
                speed: 2000,
                levels: [2, 3, 4, 5, 6, 7, 12, 16, 10, 50],
            },
            shadow: 0,
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: -1,
            stopAtSlide: -1,
            shuffle: "off",
            autoHeight: "off",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
                simplifyAll: "off",
                nextSlideOnWindowFocus: "off",
                disableFocusListener: false,
            }
        });
    }
});

/**== Header Fixed on Scroll ==**/
$(window).scroll(function() {
    if ($(window).scrollTop() >= 300) {
        $('.header_fixed_on_scroll').addClass('fixed-header');
    } else {
        $('.header_fixed_on_scroll').removeClass('fixed-header');
    }
});
