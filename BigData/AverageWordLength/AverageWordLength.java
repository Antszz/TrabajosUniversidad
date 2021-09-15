import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class AverageWordLength {

    public static class TokenizerMapper
	extends Mapper<Object, Text, Text, IntWritable>{

        private Text firstCharacter = new Text();
        private final static IntWritable length = new IntWritable(1);

	    public void map(Object key, Text value, Context context)
	      throws IOException, InterruptedException {
            StringTokenizer itr = new StringTokenizer(value.toString());
            while (itr.hasMoreTokens()) {
                String token = itr.nextToken();

                // Obtendremos el primer caracter de todas las palabras
                // Y los asociaremos con el tamaño total de la palabra
                firstCharacter.set(token.substring(0,1));
                length.set(token.length());
                context.write(firstCharacter, length);
            }
        }
    }

    public static class IntAverageReducer
	extends Reducer<Text, IntWritable, Text, DoubleWritable> {
        private DoubleWritable result = new DoubleWritable();

        public void reduce(Text key, Iterable<IntWritable> values, Context context)
          throws IOException, InterruptedException {
            double sum = 0;
            int total = 0;
            for (IntWritable val : values) {
                // Contaremos el total de letras, para al final divirdir a la suma de todos sus valores, es decir:
                // la suma de la cantidad de letras que tenia cada letra inicial
                total++;
                sum += val.get();
            }
            double average = sum / total;
            result.set(average);
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();
        String[] inputs = new GenericOptionsParser(conf, args).getRemainingArgs();

        Job job = new Job(conf, "word count");
        job.setJarByClass(AverageWordLength.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setReducerClass(IntAverageReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(inputs[0]));
        FileOutputFormat.setOutputPath(job, new Path(inputs[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}