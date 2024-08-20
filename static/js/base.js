(function($) {
    "use strict";

    $(document).ready(function() {
        // Mobile Nav toggle
        $('.menu-toggle > a').on('click', function(e) {
            e.preventDefault();
            $('#responsive-nav').toggleClass('active');
        });

        // Fix cart dropdown from closing
        $('.cart-dropdown').on('click', function(e) {
            e.stopPropagation();
        });
    });

})(jQuery);