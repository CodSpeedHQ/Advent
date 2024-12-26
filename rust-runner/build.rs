use std::env;

fn main() {
    if let Ok(day_number) = env::var("DAY_NUMBER") {
        if day_number == "25" {
            println!("cargo:rustc-cfg=day_25");
        }
    }
}
