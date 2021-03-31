import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {


    public static boolean SAT_Ver(int[][] SAT, ArrayList<Integer> V){

        boolean satisfiable = true;

        int i = 0;
        boolean clause;

        while(satisfiable && i < SAT.length){
            clause = false;
            for(int j = 0; j < V.size(); j++){
                if( SAT[i][j] == V.get(j)){
                    clause = true;
                    break;
                }
            }
            if(!clause){
                satisfiable = false;
            }
            i++;
        }


        if(satisfiable){
            System.out.print("L'instance resoud le probleme. \n");
        }
        else{
            System.out.print("L'instance ne resoud pas le probleme. \n");
        }
        return satisfiable;
    }

    // fonction qui genere un Tableau de boolean
    public static ArrayList<Integer> genererV(int m){
        ArrayList<Integer> V = new ArrayList<>();
        for(int i=0; i<m; i++){
            V.add((int) (Math.random() * 2 + 1));
        }
        return V;
    }

    // fonction qui genere une matrice SAT
    public static int[][] genererSAT(int n, int m){
        int[][] SAT = new int[n][m];
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                SAT[i][j] = (int) (Math.random() * 4 - 1);
            }
        }
        return SAT;
    }


    public static void main(String[] arg) throws IOException {

        List<Result> results = new ArrayList<>();

        Integer n = 10000, m;
        int m_min = 2000, m_max = 32000, pas = 2000;
        int taille = (int)((m_max - m_min)/pas);

        long startTime;
        long endTime;
        long duration;

        int[][] SAT;
        ArrayList<Integer> V;

        boolean value;

        for (int i=0; i<taille; i++) {
            m = m_min + (i*pas);

            SAT = genererSAT(n,m);
            V = genererV(m);

            System.out.println("n = " + n.toString( ) + ", m = " + m.toString( ));

            startTime = System.nanoTime( );
            value = SAT_Ver(SAT, V);
            endTime = System.nanoTime( );
            duration = (endTime - startTime);

            results.add(new Result(n, m, value, duration));
        }

        writeCSV(results);
    }

    public static void writeCSV(List<Result> results) throws IOException {
        FileWriter csvWriter = new FileWriter("SAT_JAVA.csv");
        csvWriter.append("n,m,value,time_exe\n");

        for (Result result : results){
            csvWriter.append(result.toString());
        }
        csvWriter.flush( );
        csvWriter.close( );
    }
}
