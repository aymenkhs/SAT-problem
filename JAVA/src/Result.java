public class Result {

    Integer n;
    Integer m;
    Integer value;
    double time_exe;

    public Result(Integer n, Integer m, boolean value, double time_exe) {
        this.n = n;
        this.m = m;
        this.value = (value) ? 1 : 0;
        this.time_exe =  time_exe / 1000000000;
    }

    @Override
    public String toString() {
        return n + "," + m + "," + value + "," + time_exe +"\n";
    }

    public Integer getN() {
        return n;
    }

    public void setN(Integer n) {
        this.n = n;
    }

    public Integer getM() {
        return m;
    }

    public void setM(Integer m) {
        this.m = m;
    }

    public Integer isValue() {
        return value;
    }

    public void setValue(Integer value) {
        this.value = value;
    }

    public double getTime_exe() {
        return time_exe;
    }

    public void setTime_exe(double time_exe) {
        this.time_exe = time_exe;
    }
}
