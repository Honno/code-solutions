function solution($N) {
    $bits_str = decbin($N);
    $bits = str_split($bits_str);

    $largest_gap = 0;
    $counting = false;
    $gap = 0;
    foreach ($bits as $bit) {
        if ($bit == "0" and $counting) {
            $gap++;
        } elseif ($bit == "1") {
            if (!$counting) {
                $counting = true;
            } else {
                if ($gap > $largest_gap) {
                    $largest_gap = $gap;
                }
                $gap = 0;
            }
        }
    }

    return $largest_gap;
}
