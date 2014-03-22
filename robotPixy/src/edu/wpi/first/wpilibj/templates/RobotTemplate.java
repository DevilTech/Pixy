

package edu.wpi.first.wpilibj.templates;


import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.SPIDevice;

public class RobotTemplate extends IterativeRobot {
  SPIDevice pixy;
    public void robotInit() {
        pixy = new SPIDevice(2,8,7,6,5);
    }

    public void autonomousPeriodic() {

    }

   
    public void teleopPeriodic() {
        System.out.println(pixy.transfer(23, 6));
    }
    
    
    public void testPeriodic() {
    
    }
    
}
