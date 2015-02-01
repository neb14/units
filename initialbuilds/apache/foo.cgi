#!/usr/bin/perl -w

use strict;
use CGI;
use CGI::Carp qw/fatalsToBrowser/;
use DBI;

#Setup CGI and print header
my $CGI = new CGI;
print $CGI->header;
my($sth)=do_sql();
do_page($sth);

sub do_page {
	my($sth) = @_;
	print " <html> <body bgcolor=\"#737373\"> <table>";
	while(( my @results = $sth->fetchrow() )) {
		print "<tr><td>@results</td></tr>";
	}
	print "</table> </html>";
}


sub do_sql {
    my($id) = @_;
###Mysql Info
    my $database="apps"; 
    my $dbhost = "10.0.0.217";
    my $options="";
    my $user="root";
    my $password="root";

###Connect to DB
    my $dbh = DBI->connect("DBI:mysql:database=$database;host=$dbhost",$user, $password, {RaiseError => 1}) or die $!;

    my $query = "SELECT * FROM content";
    my $sth = $dbh->prepare($query) or die error_page($DBI::errstr);
    $sth->execute();
    my @results;
    return($sth);
}
    



