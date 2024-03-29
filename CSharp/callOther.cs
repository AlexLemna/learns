// Executes a shell command synchronously.

public void ExecuteCommandSync(object command)
{
    try
     {
         // create the ProcessStartInfo using "cmd" as the program to be run,
         // and "/c " as the parameters.
         // Incidentally, /c tells cmd that we want it to execute the command that follows,
         // and then exit.
    System.Diagnostics.ProcessStartInfo procStartInfo =
        new System.Diagnostics.ProcessStartInfo("cmd", "/c " + command);

    // The following commands are needed to redirect the standard output.
    // This means that it will be redirected to the Process.StandardOutput StreamReader.
    procStartInfo.RedirectStandardOutput = true;
    procStartInfo.UseShellExecute = false;
    // Do not create the black window.
    procStartInfo.CreateNoWindow = true;
    // Now we create a process, assign its ProcessStartInfo and start it
    System.Diagnostics.Process proc = new System.Diagnostics.Process();
    proc.StartInfo = procStartInfo;
    proc.Start();
    // Get the output into a string
    string result = proc.StandardOutput.ReadToEnd();
    // Display the command output.
    Console.WriteLine(result);
      }
    catch (Exception objException)
      {
      // Log the exception
      }
} 


// Executes a shell command asynchronously.

public void ExecuteCommandAsync(string command)
{
   try 
   {
    Thread objThread = new Thread(new ParameterizedThreadStart(ExecuteCommandSync)); // Asynchronously starts the Thread to process the Execute command request.
    objThread.IsBackground = true; // Makes the thread a background thread.
    objThread.Priority = ThreadPriority.AboveNormal;  // Sets the Priority of the thread.
    objThread.Start(command); // Starts the thread.
   }

   catch (ThreadStartException objException) {
    // Logs the exception
   }
   
   catch (ThreadAbortException objException)
   {
    // Logs the exception
   }
   
   catch (Exception objException)
   {
    // Logs the exception
   }
}