// stepper-servo arm

$fn = 200;

eps=0;
t=0.1; // tolerance for part extrusions

stepperAxisRadius=2;
stepperAxisFlatFromDiameter=0.5;
stepperAxisFlatLength=7; // usable lengh of axis

servoA=34.5; //height from bottom to axis mount

// stepper arm
armWidth=12.6;
armHeight=5;
armLength=servoA;

servoCableSizeW=8+t;
servoCableSizeH=3+t;

difference()
{
    // body
    cube([armLength, armWidth, armHeight]);
    // hole for stepper axis
    union()
    {
        holeR=stepperAxisRadius-stepperAxisFlatFromDiameter; // max stepperAxisRadius-stepperAxisFlatFromDiameter
        holeH=1;
        translate([armLength-armWidth/2, armWidth/2, -holeH-stepperAxisFlatLength+armHeight])
        {
            // top hole
            cylinder(stepperAxisFlatLength+holeH+eps, r=holeR);
            difference()
            {
                // axis bore
                cylinder(stepperAxisFlatLength, r=stepperAxisRadius+t);
                // flat part of axis
                translate([-2*stepperAxisRadius, -stepperAxisRadius, 0])
                cube([stepperAxisRadius+stepperAxisFlatFromDiameter-t, stepperAxisRadius*2, stepperAxisFlatLength]);
            }
        }
    }
    // cable passage
    translate([-eps, (armWidth-servoCableSizeW)/2, -eps])
        cube([servoCableSizeH, servoCableSizeW, armHeight+2*eps]);
    translate([0, (armWidth-servoCableSizeW)/2, 0])
        cube([armWidth, servoCableSizeW, servoCableSizeH]);
}

// vertical arm
vArmHeight=50;
difference()
{
    cube([armHeight, armWidth, vArmHeight+armHeight]);
    // passage for servo cable
    translate([-eps, (armWidth-servoCableSizeW)/2, 0])
        cube([servoCableSizeH, servoCableSizeW, vArmHeight+armHeight]);
    translate([0, (armWidth-servoCableSizeW)/2, 0])
        cube([armWidth, servoCableSizeW, servoCableSizeH]);
}
// servo holder
// http://www.towerpro.com.tw/product/sg92r-7/
servoE=32.5; // width with brackets
servoF=16; //height from bottom to mounting brackets
servoB=22.8; //width without brackets

translate([0,0,vArmHeight+armHeight])
{
    difference()
    {
        //servo holder
        cube([armHeight+servoF, armWidth, servoE]);
        translate([armHeight-t, -eps, (servoE-servoB)/2])
            cube([servoF+eps+t, armWidth+2*eps+t, servoB+t]);
        
        // passage for servo cable
        servoCableB=8+t; // from bottom... made bigger to fit connector through
        // into bottom holder arm
        translate([-eps, (armWidth-servoCableSizeW)/2, armHeight-servoCableSizeH])
            cube([armHeight+servoCableB, servoCableSizeW, servoCableSizeH]);
        // into back of holder
        translate([-eps, (armWidth-servoCableSizeW)/2, -eps])
            cube([servoCableSizeH, servoCableSizeW, servoB+armHeight]);
        // into top holder arm
        translate([-eps, (armWidth-servoCableSizeW)/2, servoB+armHeight-eps])
            cube([armHeight+servoCableB, servoCableSizeW, servoCableSizeH]);
        
        //screw holes
        servoScrewDiameter=2-t; //M2, will screw into the printed part
        // bottom
        translate([0, armWidth/2, armHeight/2])
            rotate([0, 90, 0])
                cylinder(armHeight+servoF, d=servoScrewDiameter);
        // top
        translate([0, armWidth/2, servoB+armHeight+armHeight/2])
            rotate([0, 90, 0])
                cylinder(armHeight+servoF, d=servoScrewDiameter);        
    }
}