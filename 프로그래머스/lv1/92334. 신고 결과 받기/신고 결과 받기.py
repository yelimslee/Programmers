def solution(id_list, reports, k):
    reported = {id: set() for id in id_list}
    report_count = {id: 0 for id in id_list}
    
    for i in set(reports):
        reporter, reported_id = i.split(' ')
        reported[reported_id].add(reporter)

    for reported_id, reporters in reported.items():
        if len(reporters) >= k:
            for reporter in reporters:
                report_count[reporter] += 1

    return [report_count[id] for id in id_list]
