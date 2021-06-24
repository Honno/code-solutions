<!DOCTYPE html>
<html>
<head>
  <title>Lab 4 tasks </title>
</head>

<body>
	<h1>Lab 4 tasks</h1>

	<!-- Task 1: String-->
	<!-- write your solution to Task 1 here -->
	<div class="section">
		<h2>Task 1 : String</h2>
    <ul>
        <?php
        function li($string) {
            echo "<li>$string</li>";
        }

        $luv = "I love programming";

        li(substr($luv, 0, 1));
        li(strlen($luv));
        li(substr($luv, -1, 1));
        li(substr($luv, 0, 6));
        li(strtoupper($luv));
        ?>
    </ul>
	</div>

	<!-- Task 2: Array and image-->
	<!-- write your solution to Task 2 here -->
	<div class="section">
		<h2>Task 2 : Array and image</h2>
    <?php
    $images = glob('images/*.jpg');
    $img = $images[rand(0, sizeof($images) - 1)];
    echo "<img src=$img />"
    ?>
	</div>

	<!-- Task 3: Function definition dayinmonth  -->
	<!-- write your solution to Task 3 here -->
	<div class="section">
		<h2>Task 3 : Function definition</h2>
    <ul>
    <?php
    function daysInMonth($num) {
        return cal_days_in_month(CAL_GREGORIAN, $num, date('Y'));
    }

    for($month = 1; $month <= 12; $month++) {
        echo "<li>" . "Month $month => " . daysInMonth($month) . "days." . "</li>";
    }
    ?>
    </ul>
	</div>

	<!-- Task 4: Favorite Artists from a File (Files) -->
	<!-- write your solution to Task 4 here -->
	<div class="section">
		<h2>Task 4: My Favorite Artists from a file</h2>
    <ul>
    <?php
    $artists = file('favorite.txt');

    foreach ($artists as $artist) {
        echo "<li><a href=\"http://www.mtv.com/artists/" . str_replace(' ', '-', strtolower($artist)) . "/\">$artist</a></li>\n";
    }
    ?>
    </ul>
	</div>
	
	<!-- Task 6: Directory operations -->
	<!-- write your solution to Task 6 here -->
	<div class="section">
		<h2>Task 6 : Directory operations</h2>
    <ul>
    <?php
    foreach(scandir('.') as $file) {
        if(is_file($file)) {
            echo "<li>$file</li>\n";
        }
    }
    ?>
    </ul>
	</div>

	<!-- Task 6 optional: Directory operations -->
	<!-- write your solution to Task 6 optional here -->
	<div class="section">
		<h2>Task 6 optional: Directory operations optional</h2>
	  <?php
    function listFiles($dir, $file) {
        echo "<li>$file";
	      $path = "$dir/$file";
        echo "<ul>";
        foreach(scandir($path) as $item) {
            if(is_file($item)) {
                echo "<li>$item</li>";
            } elseif($item != '.' && $item != '..') {
                listFiles($path, $item);
            }
	      }
	      echo "</ul></li>";
    }
    echo "<ul>";
    listFiles('.', '');
    echo "</ul>";
    ?>
	</div>
	</div


	
    <!-- Task 5: including external files -->
	<!-- write your solution to Task 5 here -->
	<div class="section">
		<h2>Task 5: including external files</h2>
    <?php include 'footer.php' ?>
	</div>

</body>
</html>
