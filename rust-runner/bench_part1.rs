use codspeed_criterion_compat::{black_box, criterion_group, criterion_main, Criterion};
use rust_runner::check_result;

paste::paste! {
    use solution::[<day env!("DAY_NUMBER")>]::{part1};
}

fn bench_part1(c: &mut Criterion) {
    let mut g = c.benchmark_group(concat!("day", env!("DAY_NUMBER")));
    let input = include_str!("./input.txt");
    g.bench_function("part1", |b| b.iter(|| part1(black_box(input))));
    let output = part1(input);
    let expected = include_str!("./output-1.txt");
    check_result(output, expected, 1);
}

criterion_group!(benches, bench_part1);
criterion_main!(benches);
