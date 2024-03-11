// jQuery document ready function
$(document).ready(function(){
    // Handling clicks on dynamically loaded links
    $(document).on('click', '.dynamic-link', function(e) {
        e.preventDefault(); // Prevent the default link behavior

        var url = $(this).attr('href'); // Get the URL from the link's href attribute

        // Update the AJAX request to handle different sections of the site
        $.ajax({
            url: url,
            type: 'GET', // Specify the request type
            success: function(response) {
                // Assuming '#main-content' is the container where dynamic content should be loaded
                $('#main-content').html($(response).find('#content').html());
            },
            error: function(xhr, status, error) {
                // On error, you might want to inform the user or log the error
                console.error("Error occurred: " + error);
            }
        });
    });

    // Handling category divs for dynamic content loading
    $('.category').click(function() {
        var categoryType = $(this).attr('id'); // Using ID or a data attribute to differentiate categories
        var url = '/categories/' + categoryType; // Construct the URL based on the category type

        // Load the category-specific content dynamically
        $('#main-content').load(url + ' #content');
    });

    // Handling the "About" section specifically if needed
    $('#about-link').click(function(e){
        e.preventDefault(); // Prevent the default link behavior

        // Directly load the about section content
        $('#main-content').load('path/to/about.html #about-content'); // Ensure the path matches your setup
    });
});
function reloadPage() {
    // Logic to reload page content dynamically or simply reload the page
    window.location.reload(); // Simple page reload
}
