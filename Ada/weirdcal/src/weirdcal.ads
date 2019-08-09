-- file: weirdcal.ads
type num_day_of_month is range 1 .. 28;
type num_month_of_year is range 1 .. 13;
type num_longcount_year is Natural;
type hour is mod 24;
type minute is mod 60;
type second is mod 60;
type proper_month is (Onemonth, Twomonth, Threemonth, Fourmonth, Fivemonth, Sixmonth, Sevenmonth, Eightmonth, Ninemonth, Tenmonth, Elevenmonth, Twelvemonth, Thirteenmonth);
type proper_day_of_week is (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday);
subtype workweek is proper_day_of_week range Monday .. Friday;

type date is record
   end record
