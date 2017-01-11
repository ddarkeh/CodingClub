use strict;

sub sub_input {
my $input;
print "Please Enter your input between 0 and 10000:\n";
$input = <STDIN>;
chomp $input;

return $input;
}

my $input;
while ($input < 0 || $input > 10000 || (!$input) ) {
  $input = sub_input();

  if ($input < 0) {
    print "Input is less than 0 please try again\n";
  }
  if ($input > 10000) {
    print "Input is greater than 10000 please try again\n";
  }
  if (!$input) {
    print "Please Input a number\n";
  }
}

print "Using the number $input\n";

my @input = split//,$input;

my $total = 0;

foreach (@input) {
$total = $total + $_;
}

print "The Result is: " . $total;
print " (";
my $i = scalar @input;
my $count = 0;
foreach (@input) {

print $_;
$count++;

if ($count < ($i)) {
print "+";

}
}
print ")\n";
