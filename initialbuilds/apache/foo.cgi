#!/usr/bin/perl -w 

use strict;

print "Content-type: text/plain; charset=iso-8859-1\n\n";
my $var;
my $val;
foreach $var (sort(keys(%ENV))) {
    $val = $ENV{$var};
    $val =~ s|\n|\\n|g;
    $val =~ s|"|\\"|g;
    print "${var}=\"${val}\"\n";
}#!/usr/bin/perl -w 

use strict;

print "Content-type: text/plain; charset=iso-8859-1\n\n";
my $var;
my $val;
foreach $var (sort(keys(%ENV))) {
    $val = $ENV{$var};
    $val =~ s|\n|\\n|g;
    $val =~ s|"|\\"|g;
    print "${var}=\"${val}\"\n";
}#!/usr/bin/perl -w 

use strict;

print "Content-type: text/plain; charset=iso-8859-1\n\n";
my $var;
my $val;
foreach $var (sort(keys(%ENV))) {
    $val = $ENV{$var};
    $val =~ s|\n|\\n|g;
    $val =~ s|"|\\"|g;
    print "${var}=\"${val}\"\n";
}#!/usr/bin/perl -w 

use strict;

print "Content-type: text/plain; charset=iso-8859-1\n\n";
my $var;
my $val;
foreach $var (sort(keys(%ENV))) {
    $val = $ENV{$var};
    $val =~ s|\n|\\n|g;
    $val =~ s|"|\\"|g;
    print "${var}=\"${val}\"\n";
}
