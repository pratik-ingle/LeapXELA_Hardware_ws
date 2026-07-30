try:
    # When imported as part of the `xela_description` Python package.
    from .list_to_string import list_to_string  # noqa: F401
except ImportError:  # pragma: no cover
    # When executed directly as a script.
    from list_to_string import list_to_string  # noqa: F401


def get_sparseskin_frames() -> str:
    """Dummy links + fixed joints for sparse-skin sensor frames on the palm."""
    return """  <!-- Frame 46_ss_1 (dummy link + fixed joint) -->
  <link name="46_ss_1">
    <origin xyz="0 0 0" rpy="0 -0 0"/>
    <inertial>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <mass value="1e-9"/>
      <inertia ixx="0" ixy="0" ixz="0" iyy="0" iyz="0" izz="0"/>
    </inertial>
  </link>
  <joint name="46_ss_1_frame" type="fixed">
    <origin xyz="-0.0269 -0.027 0.048" rpy="1.5708 0 -0"/>
    <parent link="leap_hand_xela_back_cover"/>
    <child link="46_ss_1"/>
    <axis xyz="0 0 0"/>
  </joint>
  <!-- Frame 46_ss_3 (dummy link + fixed joint) -->
  <link name="46_ss_3">
    <origin xyz="0 0 0" rpy="0 -0 0"/>
    <inertial>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <mass value="1e-9"/>
      <inertia ixx="0" ixy="0" ixz="0" iyy="0" iyz="0" izz="0"/>
    </inertial>
  </link>
  <joint name="46_ss_3_frame" type="fixed">
    <origin xyz="-0.0269 -0.027 0.0811" rpy="1.5708 0 -0"/>
    <parent link="leap_hand_xela_back_cover"/>
    <child link="46_ss_3"/>
    <axis xyz="0 0 0"/>
  </joint>
  <!-- Frame 46_ss_2 (dummy link + fixed joint) -->
  <link name="46_ss_2">
    <origin xyz="0 0 0" rpy="0 -0 0"/>
    <inertial>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <mass value="1e-9"/>
      <inertia ixx="0" ixy="0" ixz="0" iyy="0" iyz="0" izz="0"/>
    </inertial>
  </link>
  <joint name="46_ss_2_frame" type="fixed">
    <origin xyz="0.0654 -0.027 0.1113" rpy="-1.5708 -0 -3.14159"/>
    <parent link="leap_hand_xela_back_cover"/>
    <child link="46_ss_2"/>
    <axis xyz="0 0 0"/>
  </joint>


  <!-- Frame 44_ss_rf_3 (dummy link + fixed joint) -->
  <link name="44_ss_rf_3">
    <origin xyz="0 0 0" rpy="0 -0 0"/>
    <inertial>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <mass value="1e-9"/>
      <inertia ixx="0" ixy="0" ixz="0" iyy="0" iyz="0" izz="0"/>
    </inertial>
  </link>
  <joint name="44_ss_rf_3_frame" type="fixed">
    <origin xyz="-0.04897 -0.026 0.153574" rpy="1.5708 1.5708 0"/>
    <parent link="leap_hand_xela_back_cover"/>
    <child link="44_ss_rf_3"/>
    <axis xyz="0 0 0"/>
  </joint>
  <!-- Frame 44_ss_mf_3 (dummy link + fixed joint) -->
  <link name="44_ss_mf_3">
    <origin xyz="0 0 0" rpy="0 -0 0"/>
    <inertial>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <mass value="1e-9"/>
      <inertia ixx="0" ixy="0" ixz="0" iyy="0" iyz="0" izz="0"/>
    </inertial>
  </link>
  <joint name="44_ss_mf_3_frame" type="fixed">
    <origin xyz="-0.00352 -0.026 0.153574" rpy="1.5708 1.5708 0"/>
    <parent link="leap_hand_xela_back_cover"/>
    <child link="44_ss_mf_3"/>
    <axis xyz="0 0 0"/>
  </joint>
  <!-- Frame 44_ss_if_3 (dummy link + fixed joint) -->
  <link name="44_ss_if_3">
    <origin xyz="0 0 0" rpy="0 -0 0"/>
    <inertial>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <mass value="1e-9"/>
      <inertia ixx="0" ixy="0" ixz="0" iyy="0" iyz="0" izz="0"/>
    </inertial>
  </link>
  <joint name="44_ss_if_3_frame" type="fixed">
    <origin xyz="0.04193 -0.026 0.153574" rpy="1.5708 1.5708 0"/>
    <parent link="leap_hand_xela_back_cover"/>
    <child link="44_ss_if_3"/>
    <axis xyz="0 0 0"/>
  </joint>"""


def get_palm_constant(sparseskin: bool = False) -> str:
    palm_link = """<link name="leap_hand_xela_back_cover">
    <inertial>
      <origin xyz="-0.000780549 -0.00686016 0.0718797" rpy="0 0 0"/>
      <mass value="0.237"/>
      <inertia ixx="0.00330843" ixy="6.79303e-05" ixz="-0.000176923" iyy="0.00420899" iyz="0.000182026" izz="0.00177685"/>
    </inertial>
    <!-- Part leap_hand_xela_motorholder -->
    <visual>
      <origin xyz="0.0180627 0.023 0.0834096" rpy="-3.14159 1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/leap_hand_xela_motorholder.stl"/>
      </geometry>
      <material name="leap_hand_xela_motorholder_material">
        <color rgba="0.792157 0.819608 0.933333 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0.0180627 0.023 0.0834096" rpy="-3.14159 1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/leap_hand_xela_motorholder.stl"/>
      </geometry>
    </collision>
    <!-- Part uspa46 -->
    <visual>
      <origin xyz="-0.005515 -0.027 0.0631" rpy="-0 -0 -3.14159"/>
      <geometry>
        <mesh filename="package://assets/uspa46.stl"/>
      </geometry>
      <material name="uspa46_material">
        <color rgba="0.792157 0.819608 0.933333 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="-0.005515 -0.027 0.0631" rpy="-0 -0 -3.14159"/>
      <geometry>
        <mesh filename="package://assets/uspa46.stl"/>
      </geometry>
    </collision>
    <!-- Part thp0_unified -->
    <visual>
      <origin xyz="0.0235627 -0.013 0.0845" rpy="-0 -0 1.5708"/>
      <geometry>
        <mesh filename="package://assets/thp0_unified.stl"/>
      </geometry>
      <material name="thp0_unified_material">
        <color rgba="0.498039 0.498039 0.498039 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0.0235627 -0.013 0.0845" rpy="-0 -0 1.5708"/>
      <geometry>
        <mesh filename="package://assets/thp0_unified.stl"/>
      </geometry>
    </collision>
    <!-- Part p5_unified -->
    <visual>
      <origin xyz="-0.03767 -0.009 0.1306" rpy="1.5708 -1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/p5_unified.stl"/>
      </geometry>
      <material name="p5_unified_material">
        <color rgba="0.980392 0.713725 0.00392157 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="-0.03767 -0.009 0.1306" rpy="1.5708 -1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/p5_unified.stl"/>
      </geometry>
    </collision>
    <!-- Part top_palm -->
    <visual>
      <origin xyz="0.00785 -0.023 0.123706" rpy="3.14159 0 3.14159"/>
      <geometry>
        <mesh filename="package://assets/top_palm.stl"/>
      </geometry>
      <material name="top_palm_material">
        <color rgba="0.792157 0.819608 0.933333 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0.00785 -0.023 0.123706" rpy="3.14159 0 3.14159"/>
      <geometry>
        <mesh filename="package://assets/top_palm.stl"/>
      </geometry>
    </collision>
    <!-- Part p5_unified_2 -->
    <visual>
      <origin xyz="0.00778 -0.009 0.1306" rpy="1.5708 -1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/p5_unified.stl"/>
      </geometry>
      <material name="p5_unified_2_material">
        <color rgba="0.980392 0.713725 0.00392157 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0.00778 -0.009 0.1306" rpy="1.5708 -1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/p5_unified.stl"/>
      </geometry>
    </collision>
    <!-- Part uspa46_2 -->
    <visual>
      <origin xyz="-0.005515 -0.027 0.0962" rpy="-0 -0 -3.14159"/>
      <geometry>
        <mesh filename="package://assets/uspa46.stl"/>
      </geometry>
      <material name="uspa46_2_material">
        <color rgba="0.792157 0.819608 0.933333 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="-0.005515 -0.027 0.0962" rpy="-0 -0 -3.14159"/>
      <geometry>
        <mesh filename="package://assets/uspa46.stl"/>
      </geometry>
    </collision>
    <!-- Part p5_unified_3 -->
    <visual>
      <origin xyz="0.05323 -0.009 0.1306" rpy="1.5708 -1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/p5_unified.stl"/>
      </geometry>
      <material name="p5_unified_3_material">
        <color rgba="0.980392 0.713725 0.00392157 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0.05323 -0.009 0.1306" rpy="1.5708 -1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/p5_unified.stl"/>
      </geometry>
    </collision>
    <!-- Part uspa46_3 -->
    <visual>
      <origin xyz="0.044015 -0.027 0.0962" rpy="-3.14159 0 -0"/>
      <geometry>
        <mesh filename="package://assets/uspa46.stl"/>
      </geometry>
      <material name="uspa46_3_material">
        <color rgba="0.792157 0.819608 0.933333 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0.044015 -0.027 0.0962" rpy="-3.14159 0 -0"/>
      <geometry>
        <mesh filename="package://assets/uspa46.stl"/>
      </geometry>
    </collision>
    <!-- Part leap_hand_xela_back_cover -->
    <visual>
      <origin xyz="-0.0293149 0.023 0.131221" rpy="-0 -1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/leap_hand_xela_back_cover.stl"/>
      </geometry>
      <material name="leap_hand_xela_back_cover_material">
        <color rgba="0.792157 0.819608 0.933333 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="-0.0293149 0.023 0.131221" rpy="-0 -1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/leap_hand_xela_back_cover.stl"/>
      </geometry>
    </collision>
    <!-- Part leap_hand_xela_side_cover -->
    <visual>
      <origin xyz="-0.0503368 0 0.110009" rpy="1.5708 0.00518834 -0"/>
      <geometry>
        <mesh filename="package://assets/leap_hand_xela_side_cover.stl"/>
      </geometry>
      <material name="leap_hand_xela_side_cover_material">
        <color rgba="0.792157 0.819608 0.933333 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="-0.0503368 0 0.110009" rpy="1.5708 0.00518834 -0"/>
      <geometry>
        <mesh filename="package://assets/leap_hand_xela_side_cover.stl"/>
      </geometry>
    </collision>
    <!-- Part leap_hand_xela_bottom -->
    <visual>
      <origin xyz="0 -0.023 0.0425" rpy="3.14159 0 3.14159"/>
      <geometry>
        <mesh filename="package://assets/leap_hand_xela_bottom.stl"/>
      </geometry>
      <material name="leap_hand_xela_bottom_material">
        <color rgba="0.792157 0.819608 0.933333 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 -0.023 0.0425" rpy="3.14159 0 3.14159"/>
      <geometry>
        <mesh filename="package://assets/leap_hand_xela_bottom.stl"/>
      </geometry>
    </collision>
    <!-- Part palm_face -->
    <visual>
      <origin xyz="-0.0283776 -0.029 0.131221" rpy="-0 -1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/palm_face.stl"/>
      </geometry>
      <material name="palm_face_material">
        <color rgba="0.792157 0.819608 0.933333 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="-0.0283776 -0.029 0.131221" rpy="-0 -1.5708 0"/>
      <geometry>
        <mesh filename="package://assets/palm_face.stl"/>
      </geometry>
    </collision>
  </link>"""
    if sparseskin:
        return f"{palm_link}\n{get_sparseskin_frames()}"
    return palm_link


def render_palm_joints_urdf(sparseskin: bool = False) -> str:
    palm_link = get_palm_constant(sparseskin=sparseskin)
    return f"""
  <?xml version="1.0" ?>
  <robot name="xela_palm_generated">
  {palm_link}
  </robot>
  """.rstrip("\n")


def write_palm_urdf(file_path: str, sparseskin: bool = False) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(render_palm_joints_urdf(sparseskin=sparseskin))


if __name__ == "__main__":
    import argparse
    import os

    parser = argparse.ArgumentParser(description="Generate palm URDF.")
    parser.add_argument(
        "--sparseskin",
        action="store_true",
        default=False,
        help="Include sparse-skin sensor frames on the palm",
    )
    parser.add_argument(
        "-o",
        "--out",
        default=None,
        help="Output URDF path (default: OUT env or palm.urdf)",
    )
    args = parser.parse_args()

    out_path = args.out or os.environ.get("OUT") or "palm.urdf"
    write_palm_urdf(out_path, sparseskin=args.sparseskin)

