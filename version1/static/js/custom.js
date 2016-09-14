

// open the contact modal
$(".contactBtn").click(function() {
    $(".contactModal").css("display","block");
    return false;
});
// close the contact modal
$(".contactModal-close").click(function() {
    $(".contactModal").css("display","none");
    return false;
});