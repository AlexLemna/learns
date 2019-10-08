-- file: Ada2Python.ads

package Ada2Python is

   procedure Say_Hello;
   pragma Export (C, Say_Hello, "say_hello");

end Ada2Python;
