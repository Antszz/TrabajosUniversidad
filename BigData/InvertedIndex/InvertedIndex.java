import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class InvertedIndex {

    public static class InvertedIndexMapper extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable> {
        private final static Text word = new Text();
        private final static Text location = new Text();

        public void map(LongWritable key, Text val, OutputCollector<Text, IntWritable> output, Reporter reporter)
                        throws IOException {
            // get the filename where this line came from
            FileSplit fileSplit = (FileSplit)reporter.getInputSplit();
            IntWritable fileNo = new IntWritable(Integer.parseInt(fileSplit.getPath().getName()));

            String line = val.toString();
            StringTokenizer itr = new StringTokenizer(line.toLowerCase());

            while (itr.hasMoreTokens()) {
                word.set(itr.nextToken());
                output.collect(word, fileNo);
            }
        }
    }

	public static class InvertedIndexReducer extends MapReduceBase implements Reducer<Text, IntWritable, Text, Text> {
        private final static HashSet<IntWritable> files = new HashSet<IntWritable>();

        public void reduce(Text key, Iterator<IntWritable> values, OutputCollector<Text, Text> output, Reporter reporter)
                throws IOException {
            files.clear();

            int count=0;
            StringBuilder toReturn = new StringBuilder();
            StringBuilder keyfreq = new StringBuilder();
            System.out.println("values"+values);
            while (values.hasNext()){

                IntWritable filename = values.next();
                System.out.println("value.next" + filename );
                if( !(files.contains(filename))){
                    files.add(filename);

                    if (count!=0)
                        toReturn.append("-> ");

                    count++;
                    toReturn.append(filename);
                }
            }
            IntWritable freq = new IntWritable(count);
            keyfreq.append(key.toString());
            keyfreq.append("|");
            keyfreq.append(freq);
            output.collect(new Text(keyfreq.toString()), new Text(toReturn.toString()));
        }
    }

	public static void run(String input, String output){
        JobClient client = new JobClient();
        JobConf conf = new JobConf(InvertedIndex.class);

        conf.setJobName("InvertedIndex");

        conf.setOutputKeyClass(Text.class);
        conf.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(conf, new Path(input));
        FileOutputFormat.setOutputPath(conf, new Path(output));

        conf.setMapperClass(InvertedIndexMapper.class);
        conf.setReducerClass(InvertedIndexReducer.class);

        client.setConf(conf);

        try {
            JobClient.runJob(conf);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        if( args.length != 2 ){
            System.err.println("InvertedIndex <input_dir> <output_dir>");
        }else{
            run(args[0], args[1]);
        }
    }

}