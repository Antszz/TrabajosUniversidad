import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class BigramCount {

    public static class TokenizerMapper
        extends Mapper<Object, Text, Text, IntWritable>{

        private final static IntWritable one = new IntWritable(1);
        private Text bigram = new Text();

        public void map(Object key, Text value, Context context
                ) throws IOException, InterruptedException {
            StringTokenizer itr = new StringTokenizer(value.toString());

            Text word1 = new Text();
            word1.set("");
            if(itr.hasMoreTokens()){
                word1.set(itr.nextToken());
            }
            Text word2 = new Text();
            word2.set("");

            Text all_bigrams = new Text();
            all_bigrams.set("All Bigrams: ");

            while (itr.hasMoreTokens()) {
                word2.set(itr.nextToken());
                // Hacemos esto para no asociar palabras con otro string vacio y se generen bigramas falsos
                if(((Text) word1).toString().equals("") || ((Text) word2).toString().equals("")){
                    continue;
                }
                // con replaceAll("\\p{Punct}", "") limpiamos la data de los signos de puntuacion
                bigram.set(((Text) word1).toString().replaceAll("\\p{Punct}", "") + ' ' + ((Text) word2).toString().replaceAll("\\p{Punct}", ""));
                context.write(bigram, one);
                word1 = word2;
                // De esta manera contamos el total de bigramas
                context.write(all_bigrams, one);
            }
        }
    }

    public static class IntSumReducer
        extends Reducer<Text,IntWritable,Text,IntWritable> {
        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> values,
                        Context context
                        ) throws IOException, InterruptedException {
            int sum = 0;
            // contaremos cuantas veces se repite un bigrama
            for (IntWritable val : values) {
                sum += val.get();
            }
            result.set(sum);
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "word count");
        job.setJarByClass(BigramCount.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
