-- file: weirdcal.ads
package Antikythera_Calendar is
   subtype calendar_year is Integer range 1 .. Integer`Last;
   subtype duration_of_day is Duration range 0.0 .. 86_400.00;

   subtype num_day_of_year is Integer range 1 .. 365;
   subtype num_month_of_year is Integer range 1 .. 13;

   subtype num_day_of_month is Integer range 1 .. 28;

   is_in_current_epoch : Boolean := True

end Antikythera_Calendar;
