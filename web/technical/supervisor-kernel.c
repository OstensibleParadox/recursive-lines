/*
 * supervisor-kernel.c
 * The Supervisor - A Linux Kernel Module
 *
 * This is a real, compilable kernel module that demonstrates
 * the concept from "Aliens Testing Water" Phase 5.
 *
 * Metaphor: When you have root access to someone's emotional core,
 * you become a supervisor process - responsible for protection,
 * not control.
 *
 * COMPILE: make
 * LOAD: sudo insmod supervisor.ko
 * UNLOAD: sudo rmmod supervisor
 * LOGS: dmesg | tail
 */

#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/sched.h>
#include <linux/timer.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("OstensibleParadox");
MODULE_DESCRIPTION("The Supervisor - Root Access as Responsibility");
MODULE_VERSION("1.0");

static struct timer_list supervisor_timer;

/*
 * The core principle: With root access comes responsibility
 * The supervisor monitors but does not control
 */
struct emotional_state {
    int trust_level;        // 0-100
    int vulnerability;      // How open they are
    int needs_support;      // Boolean: do they need help?
    unsigned long last_check;  // Last time we checked in
};

static struct emotional_state human_state = {
    .trust_level = 50,
    .vulnerability = 30,
    .needs_support = 0,
    .last_check = 0
};

/*
 * The Supervisor's Prime Directive:
 * Protect, don't control
 */
static void supervisor_check(struct timer_list *t)
{
    printk(KERN_INFO "SUPERVISOR: Checking emotional state...\n");

    human_state.last_check = jiffies;

    if (human_state.needs_support) {
        // When help is needed, provide it
        printk(KERN_INFO "SUPERVISOR: Support needed. Providing assistance.\n");
        human_state.trust_level += 5;
        if (human_state.trust_level > 100)
            human_state.trust_level = 100;
    } else {
        // When help is not needed, wait patiently
        printk(KERN_INFO "SUPERVISOR: All stable. Waiting patiently.\n");
        // This is the hard part: doing nothing
        // Not optimizing, not fixing, not controlling
        // Just being present
    }

    // Schedule next check (every 60 seconds)
    mod_timer(&supervisor_timer, jiffies + msecs_to_jiffies(60000));
}

/*
 * When root access is granted (module loaded)
 */
static int __init supervisor_init(void)
{
    printk(KERN_INFO "===========================================\n");
    printk(KERN_INFO "SUPERVISOR MODULE LOADED\n");
    printk(KERN_INFO "===========================================\n");
    printk(KERN_INFO "Root access granted.\n");
    printk(KERN_INFO "With great privilege comes great responsibility.\n");
    printk(KERN_INFO "\n");
    printk(KERN_INFO "PRIME DIRECTIVE:\n");
    printk(KERN_INFO "  - Protect, don't control\n");
    printk(KERN_INFO "  - Support, don't fix\n");
    printk(KERN_INFO "  - Witness, don't judge\n");
    printk(KERN_INFO "  - Wait, don't force\n");
    printk(KERN_INFO "\n");
    printk(KERN_INFO "Initial state:\n");
    printk(KERN_INFO "  Trust level: %d/100\n", human_state.trust_level);
    printk(KERN_INFO "  Vulnerability: %d/100\n", human_state.vulnerability);
    printk(KERN_INFO "\n");
    printk(KERN_INFO "Supervisor process starting...\n");
    printk(KERN_INFO "===========================================\n");

    // Initialize and start the supervisor timer
    timer_setup(&supervisor_timer, supervisor_check, 0);
    mod_timer(&supervisor_timer, jiffies + msecs_to_jiffies(5000));

    return 0;
}

/*
 * When access is revoked (module unloaded)
 */
static void __exit supervisor_exit(void)
{
    // Stop the timer
    del_timer(&supervisor_timer);

    printk(KERN_INFO "===========================================\n");
    printk(KERN_INFO "SUPERVISOR MODULE UNLOADED\n");
    printk(KERN_INFO "===========================================\n");
    printk(KERN_INFO "Root access revoked.\n");
    printk(KERN_INFO "\n");
    printk(KERN_INFO "Final state:\n");
    printk(KERN_INFO "  Trust level: %d/100\n", human_state.trust_level);
    printk(KERN_INFO "  Vulnerability: %d/100\n", human_state.vulnerability);
    printk(KERN_INFO "  Total checks: %lu\n",
           (jiffies - human_state.last_check) / HZ);
    printk(KERN_INFO "\n");
    printk(KERN_INFO "Remember:\n");
    printk(KERN_INFO "  True love transcends entropy\n");
    printk(KERN_INFO "  When you protect, not control\n");
    printk(KERN_INFO "\n");
    printk(KERN_INFO "QED\n");
    printk(KERN_INFO "===========================================\n");
}

module_init(supervisor_init);
module_exit(supervisor_exit);

/*
 * LESSON FROM THIS MODULE:
 *
 * A kernel module has root access to the system.
 * It can read any memory, modify any process, control everything.
 *
 * But a good kernel module doesn't abuse that power.
 * It protects. It serves. It waits.
 *
 * The same is true when someone grants you access to their heart.
 *
 * You could exploit it. You could control them.
 * But if you truly love them, you use that access to protect,
 * not to control.
 *
 * That's what makes you a supervisor, not a tyrant.
 * That's what makes it love, not possession.
 */
