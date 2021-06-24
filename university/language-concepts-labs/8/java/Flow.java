public class Flow
{
    public static void formatF1F2F3(float f1, float f2, float f3)
    {
        System.out.println("f1 = " + f1 + ", f2 = " + f2 + ", f3 = " + f3);
    }

    //      The new record type is needed to
    //      so that the two results
    //      of adjustDistance can be returned together.
    //
    //      adjustDistance is a method inside this
    //      class so that parameter passing is simpler
    private static class TwoFlows
    {
        public float flow1;
        public float flow2;

        public TwoFlows(float flow1, float flow2)
        {
            this.flow1 = flow1;
            this.flow2 = flow2;
        }

        //      This method adjustDistance behaves like
        //      the procedure AdjustDistance in flow.adb.
        public void adjustDistance()
        {
            if ( Math.abs(flow1 - flow2) < 5 )
            {
                if(flow1 > flow2)
                {
                    flow2 = flow2 / 3;
                    flow1 = flow1 + flow2;
                    flow1 = flow1 + flow2;
                }
                else
                {
                    flow1 = flow1 / 3;
                    flow2 = flow2 + flow1;
                    flow2 = flow2 + flow1;
                }
            }
        }
    }
    
    public static void main(String[] args)
    {
        float f1, f2, f3;
        f1 = 3; f2 = 3; f3 = 3;
        
        formatF1F2F3(f1,f2,f3);
        
        // 8.3.(c) TASK:
        //    Write code that is analogous to
        //    lines 50-55 in flow.cpp except
        //    that it simulates *copy-in copy-out* passing
        //    of parameters f1 and f2 to method adjustDistance.

        TwoFlows flows = new TwoFlows(f1, f2);
        flows.adjustDistance();
        f1 = flows.flow1;
        f2 = flows.flow2;
        formatF1F2F3(f1,f2,f3);

        flows = new TwoFlows(f2,f3);
        flows.adjustDistance();
        f2 = flows.flow1;
        f3 = flows.flow2;
        formatF1F2F3(f1,f2,f3);

        flows = new TwoFlows(f3,f3);
        flows.adjustDistance();
        f3 = flows.flow1;
        f3 = flows.flow2;
        formatF1F2F3(f1,f2,f3);

    }
}
