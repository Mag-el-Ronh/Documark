# Crash Load Case — Knee Mapping & Impact Evaluation (Setup)

## Purpose
- Prepare FE model for Euro NCAP-compliant lower-body impact evaluation  
- Ensure realistic occupant positioning and restraint system configuration

## Dummy, Seat & Seatbelt Setup
- **Seat:** Import and align seat geometry with correct H-point & seating posture via ANSA/VE  
- **Virtual Dummy:** Position ATD H395% driver side & ATD H350/95% passenger side per EU NCAP via VE  
- **Seatbelt:** Model retractor, pretensioner, and anchor points; verify routing over dummy | referenced in Belt-Module  
- **Preloading:** Apply initial belt tension and dummy settling via VE, ProDSiG & Belt-Module tools

## Boundary Conditions
- Vehicle model fixed at global mounts; surrounding structure included for realistic load paths  
- Define initial velocity and either standard or test pulse loading  
- Airbag modules activated for knee-mapping

## Pre-Run Checks
- Dummy contact definitions (skin-to-dashboard, knees-to-lower dashboard)  
- Seatbelt retraction and pretension behavior under initial load step  
- Ensure all sensors/channels (femur force, pelvis displacement) are active

<img src="https://github.com/Dummy-Seater/Dummy-Seater-Automation/blob/main/Docu/Images/Knee-impact-setup.png" alt="Knee-impact-setup" width="50%" />

---

# Dummy, Seat & Belt Positioning Automation

## Goal
- Automate realistic occupant positioning and restraint system setup for crash simulations  
- Ensure reproducibility and regulatory compliance (e.g., Euro NCAP)

## Step Overview
- **🧍 Dummy Positioning:** Align dummy H-point and posture using VE/ANSA. Apply anthropometric rules and validate anatomical alignment  
- **🪑 Seat Preloading:** Simulate gravity-based settling of dummy on seat via quasi-static analysis. Capture seat deformation and contact forces  
- **🔗 Belt System Setup (Parametric):**  
  - Use parameter-driven inputs for layout and routing  
  - Apply initial tension (20–50 N) and define contact/friction with dummy  
  - Automate geometry creation and meshing via Belt-Module, VE, or Python scripts

## Tools Referenced
- VE, ProDSiG, Belt-Module, ANSA

<img src="https://github.com/Dummy-Seater/Dummy-Seater-Automation/blob/main/Docu/Images/Knee-impact-setup.png" alt="Knee-impact-setup" width="50%" />

---

## 🧍 Step 1: Dummy on Seat Positioning

**Goal:**  
Position the virtual dummy on the seat with anatomically correct posture and regulatory alignment.

**Sub-steps:**
- **Extract Seat Reference Geometry:** Identify key features such as the H-point, cushion surface, and backrest orientation.
- **Select Dummy Model (e.g., ATD H395):** Load a virtual FEM dummy compatible with LS-DYNA for occupant simulation.
- **Apply Position File for Setup:** Use a structured text-based position file to define joint targets, part groups, and posture constraints.
- **Align Pelvis & Torso:** Position the pelvis at the H-point and orient the torso and limbs based on seat geometry and posture rules.
- **Apply Anthropometric Rules:** Enforce joint angles and limb placement using Euro NCAP or internal protocol specifications.
- **Validate Pose & Metrics:** Confirm head height, knee angle, and overall anatomical alignment. Log metrics for reproducibility.
- **Automate via VE or ANSA:** Use positioning tools to apply constraints from the position file and streamline setup.

---

# 🪑 Step 2: Seat Preloading

## Goal
- Simulate realistic seat deformation and occupant settling using a shelf-form Regal dummy  
- Ensure accurate contact forces and boundary conditions for downstream crash analysis

## Sub-steps
- **Import & Validate Seat Geometry:** Load seat model and verify mesh quality, material setup, and connectivity  
- **Apply Dummy Position from Step 1:** Transfer joint locations and enforce posture via joint constraints or prescribed motion  
- **Activate Gravity & Mass:** Introduce dummy weight and gravity to simulate natural settling  
- **Contact & Constraint Setup:**  
  - Define surface-to-surface contact with friction  
  - Fix seat mounts and apply joint constraints  
- **Run Preload Simulation:** Perform quasi-static analysis to capture seat compression and dummy settling  
- **Export Preloaded State:** Save deformed seat and dummy configuration for use in crash setup

---

# 🔗 Step 3: Belt Routing and Tensioning

## Goal
- Model realistic seatbelt geometry and apply initial tension for accurate restraint behavior  
- Ensure routing conforms to dummy posture and regulatory standards

## Sub-steps
- **Import Final Geometry:** Load the preloaded seat and final positioned dummy  
- **Define Belt System (Parametric):**  
  - Model retractor, buckle, anchor points, and webbing  
  - Use parameter-driven inputs  
  - Specify 2D belt geometry length and 1D beam-like connectors  
  - Automate geometry creation and meshing  
- **Route Belt over Dummy:** Align belt path over shoulder, chest, and pelvis  
- **Apply Initial Tension:** Simulate realistic retractor pull-in (20–50 N preload)  
- **Contact & Constraint Setup:** Define contact with friction and constrain belt ends  
- **Validation & Export:**  
  - Verify routing, tension force, and contact pressure  
  - Export final forms for crash simulation

---

# Crash Load Case — Knee Mapping & Impact Evaluation (Analysis)

## Analysis Overview
- Non-linear transient dynamic simulation of driver and passenger knee impacts  
- Load cases derived from Euro NCAP protocols  
- Full occupant restraint system interaction included

## Key Evaluation Metrics
- **Femur Force:** ≤ 3.8 kN  
- **Knee Displacement & Sliding:** ≤ 6 mm  
- **Belt Loads & Restraint Response:** Evaluate seatbelt forces and dummy kinematics  
- **Energy Absorption & Plastification:** Confirm plastic strains within limits

## Postprocessing & Reporting
- Extract sensor data  
- Generate automated reports  
- Highlight limit exceedances

## Outcome & Next Steps
- **Pass:** Dashboard design approved  
- **Fail:** Modify design, materials, or restraint setup; re-run analyses

<img src="https://github.com/Dummy-Seater/Dummy-Seater-Automation/blob/main/Docu/Images/KM-load-bg.svg" alt="Knee-impact-setup" width="100%" />

---

