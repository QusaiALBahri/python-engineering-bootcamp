# Day 8: Agile Sprints & Project Management

## Overview

In real projects, developers work in **sprints** - short cycles of 1-2 weeks where you:
1. Plan features (user stories)
2. Implement and test
3. Review and refine

This day simulates a real sprint with buggy code for you to fix.

---

## Part 1: User Stories & Tasks

### Sprint Goal: Build a Task Management System

**User Story 1**: As a user, I want to create tasks with titles and descriptions
**User Story 2**: As a user, I want to mark tasks complete
**User Story 3**: As a user, I want to save tasks to a file

---

## Part 2: Agile Workflow

### Sprint 1 Code (BUGGY - has 5 bugs #801-805)

See `task_manager_bug_v1.py` - Find and fix these bugs:
- **Bug #801**: Tasks never load from file
- **Bug #802**: Completed task count is wrong
- **Bug #803**: No validation on task names
- **Bug #804**: Can't delete completed tasks
- **Bug #805**: File format inconsistent

### Sprint 2 Code (HARDENED - fixed version)

See `task_manager_hardened_v2.py` - Professional version with:
- Type hints and docstrings
- Input validation
- Proper error handling
- Logging throughout
- Clean file persistence

---

## Part 3: Working in Agile

### What You'll Learn

1. **Identify bugs** through testing and logging
2. **Debug systematically** - trace execution, check assumptions
3. **Fix incrementally** - one bug at a time
4. **Test after each fix** - confirm it works
5. **Review code quality** - compare against hardened version

### Tools You'll Use

```bash
# Run and test
python task_manager_bug_v1.py

# Check for errors
# Add logging to find bugs
# Compare with hardened version
python task_manager_hardened_v2.py
```

---

## Key Principles

### 1. Test-Driven Development (TDD)
- Write test first
- Watch it fail
- Write code to pass test
- Refactor

### 2. Continuous Integration
- Run tests constantly
- Catch bugs early
- Never break existing functionality

### 3. Code Review
- Another person reviews
- Learns from professionals
- Shares knowledge

---

## Your Sprint Tasks

1. ✅ Understand the feature (task management)
2. ✅ Run buggy code and see failures
3. ✅ Fix bug #801 (file loading)
4. ✅ Fix bug #802 (completed count)
5. ✅ Fix bug #803 (validation)
6. ✅ Fix bug #804 (deletion)
7. ✅ Fix bug #805 (file format)
8. ✅ Test with edge cases
9. ✅ Compare with hardened version
10. ✅ Document what you learned

---

## Professional Agile Terms

| Term | Meaning |
|------|---------|
| **Sprint** | 1-2 week cycle of work |
| **User Story** | Feature from user perspective |
| **Task** | Specific work item |
| **Bug** | Feature not working correctly |
| **Ticket** | Bug or feature with description |
| **Backlog** | List of work to do |
| **Burndown** | Progress of sprint completion |
| **Retrospective** | Team learns from sprint |

---

## Daily Standup (What You'll Do)

Every day in a real sprint:
- What did I complete yesterday?
- What will I complete today?
- What's blocking me?

Example for Day 8:
```
Yesterday: Set up project, understand requirements
Today: Fix bugs #801-803
Blocking: Need to understand logging
```

---

## Next Steps

1. Open `task_manager_bug_v1.py`
2. Read through the code
3. Run it and see what fails
4. See `TICKETS.md` for detailed bug descriptions
5. Fix bugs one at a time
6. Test after each fix
7. Compare with `task_manager_hardened_v2.py`
8. Complete EXERCISES.md

---

## Key Takeaways

1. **Real projects have bugs** - That's normal, not failure
2. **Debugging is a skill** - Gets faster with practice
3. **Agile is iterative** - Small steps, frequent testing
4. **Code review prevents bugs** - Compare against professionals
5. **Logging helps debugging** - Add print/logging strategically
6. **Test constantly** - Catch failures early
