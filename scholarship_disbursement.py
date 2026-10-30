'''Scholarship disbursement module.'''
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE awards ("
    "id INTEGER PRIMARY KEY, student TEXT, scheme TEXT, "
    "amount INTEGER, disbursed INTEGER)"
)


def grant(student, scheme, amount, audit=None):
    """Grant a scholarship award and record the student in the audit list."""
    if audit is None:
        audit = []

    conn.execute(
        "INSERT INTO awards (student, scheme, amount, disbursed) "
        "VALUES (?, ?, ?, 0)",
        (student, scheme, amount),
    )
    audit.append(student)
    return audit


def disburse(award_id):
    """Disburse an award and return its amount, or zero if not found."""
    row = conn.execute(
        "SELECT amount FROM awards WHERE id = ?", (award_id,)
    ).fetchone()

    if row:
        conn.execute(
            "UPDATE awards SET disbursed = 1 WHERE id = ?", (award_id,)
        )
        conn.commit()
        return row[0]

    return 0


def get_disbursed_total():
    """Return the total amount currently marked as disbursed."""
    row = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM awards WHERE disbursed = 1"
    ).fetchone()
    return row[0]


def archive():
    """Record that scholarship awards have been archived."""
    print("archiving awards")


def by_scheme_count(scheme):
    """Return the number of awards for the given scholarship scheme."""
    if scheme is None:
        return 0

    return conn.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?", (scheme,)
    ).fetchone()[0]


def main():
    """Run a small scholarship disbursement demonstration."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)
    print(disburse(1), disburse(9))
    print(by_scheme_count("Merit"), get_disbursed_total())
    archive()


main()
