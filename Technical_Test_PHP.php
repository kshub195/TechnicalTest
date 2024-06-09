<?php
$date1 = date_create("2024-01-10");
$date2 = date_create("2024-06-10");

function differenceBetweenDates($date1, $date2) {
    $diff = date_diff($date1, $date2);
    
    //Format days
    $daysDifference = abs($diff->format("%a"));
	
    //Check even or odd
    $oddOrEven = ($daysDifference % 2 == 0) ? "even" : "odd";
    
    echo "The number of days between " . date_format($date1, "Y-m-d") . " and " . date_format($date2, "Y-m-d") . " is $daysDifference days, the days are $oddOrEven";
}

differenceBetweenDates($date1, $date2);
?>
