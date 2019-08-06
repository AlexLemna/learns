using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Pipes;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace UI
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        /// <summary>
        /// Declaring variables.
        /// </summary>
        int count = 0;
        private readonly object _lock = new object();
        private readonly Queue<string> _queue = new Queue<string>();
        private readonly AutoResetEvent _signal = new AutoResetEvent(false);
        delegate void StringArgReturningVoidDelegate(string text, Label L);
        private static NamedPipeServerStream server_stream;
        private BinaryReader br;
        private BinaryWriter bw;


        public MainWindow()
        {
            InitializeComponent();
            server_stream = new NamedPipeServerStream ("stream1");
            br = new BinaryReader (server_stream);
            bw = new BinaryWriter (server_stream);
            new Thread (new ThreadStart (ProducerThread)).Start();
        }


        void ProducerThread()
        {
            while (true)
            {
                _signal.WaitOne();
                string item = string.Empty;
                do
                {
                    item = string.Empty;
                    lock (_lock)
                    {
                        if (_queue.Count > 0)
                        {
                            item = _queue.Dequeue();
                            /// Need to look up the code for interacting with labels in WPF.
                        }
                    }
                    if (item != string.Empty)
                    {
                        try /// WIP. Pick up at line 83 of Main.cs
                        { }
                    }
                }
            }
        }
    }
}
