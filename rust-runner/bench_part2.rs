use codspeed_criterion_compat::{black_box, criterion_group, criterion_main, Criterion};
use rust_runner::check_result;

paste::paste! {
    use solution::[<day env!("DAY_NUMBER")>]::{part2};
}

fn bench_part2(c: &mut Criterion) {
    let mut g = c.benchmark_group(concat!("day", env!("DAY_NUMBER")));
    let input = include_str!("./input.txt");
    g.bench_function("part2", |b| b.iter(|| part2(black_box(input))));
    let output = part2(input);
    let expected = include_str!("./output-2.txt");
    check_result(output, expected, 2);
}

criterion_group!(benches, bench_part2);
criterion_main!(benches);
