package edu.wpi.first.wpilibj.templates;

import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.SPIDevice;

public class RobotTemplate extends IterativeRobot {

  Pixy p;

    public void robotInit() {
        p = new Pixy(5);
    }

    public void autonomousPeriodic() {

    }

    public void disabledPeriodic() {

    }

    public void disabledInit() {
        System.out.println("init");
        while (true) {
            byte[] b = p.read();
            if(b[0] != 0)
            for(int i = 0; i < b.length; i++)
                System.out.print(b[i] +"," );
            System.out.print("\n");
        }
    }

    public void teleopPeriodic() {

    }

    public void testPeriodic() {

    }

}
