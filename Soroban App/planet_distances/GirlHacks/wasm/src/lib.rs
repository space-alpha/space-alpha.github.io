use dialoguer::Select;

#[no_mangle]
pub extern "C" fn run_rust_code() -> *const u8 {
    // Define the distances from the Sun to planets in kilometers.
    let distances_to_sun: Vec<(&str, i64)> = vec![
        ("Mercury", 57900000),
        ("Venus", 108200000),
        ("Earth", 149600000),
        ("Mars", 227900000),
        ("Jupiter", 778300000),
        ("Saturn", 1427000000),
        ("Uranus", 2871000000),
        ("Neptune", 4497000000),
    ];

    // Create a list of planet names for the dropdown menu.
    let planet_names: Vec<&str> = distances_to_sun.iter().map(|(name, _)| *name).collect();

    // Declare the select1 and select2 variables as mutable.
    let mut select1 = Select::new();
    let mut select2 = Select::new();

    // Display a dropdown menu for the user to select the first planet.
    let planet1 = select1
        .with_prompt("Select the first planet:")
        .items(&planet_names)
        .default(0) // Default selection (Mercury in this case)
        .interact()
        .unwrap();

    // Display a dropdown menu for the user to select the second planet.
    let planet2 = select2
        .with_prompt("Select the second planet:")
        .items(&planet_names)
        .default(0) // Default selection (Mercury in this case)
        .interact()
        .unwrap();

    let (planet1, distance1) = distances_to_sun[planet1];
    let (planet2, distance2) = distances_to_sun[planet2];

    // Calculate the absolute difference between distances.
    let distance_between_planets = (distance1 - distance2).abs();

    // Format the result as a string.
    let result = format!(
        "Distance between {} and {} is {} km",
        planet1, planet2, distance_between_planets
    );

    // Convert the result to a C-compatible string.
    let c_string = std::ffi::CString::new(result).unwrap();

    // Leak the C string and return a pointer to it.
    c_string.into_raw()
}
