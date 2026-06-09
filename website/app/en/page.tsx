import styles from '../page.module.css'
import Link from 'next/link'

export default function EnglishHome() {
  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <div className={styles.heroSection}>
          <h1 className={styles.title}>
            AI Landscape
          </h1>
          
          <p className={styles.subtitle}>
            A definitive guide for full-stack developers to navigate the AI ecosystem. 
            From foundational models to infrastructure and autonomous agents.
          </p>
          
          <div className={styles.actionContainer}>
            <Link href="/en/docs/00-guides-and-trends/ecosystem-map" className={styles.primaryBtn}>
              Read the Documentation
            </Link>
            <a href="https://github.com/LuckyOneTwoThree/ai-landscape" target="_blank" rel="noreferrer" className={styles.secondaryBtn}>
              GitHub
            </a>
          </div>

          <div className={styles.trendingSection}>
            <span className={styles.trendingLabel}>🔥 Trending:</span>
            <Link href="/en/docs/01-foundation-models/llm" className={styles.trendingLink}>Local LLMs</Link>
            <Link href="/en/docs/02-infrastructure/vector-db" className={styles.trendingLink}>Vector & RAG</Link>
            <Link href="/en/docs/10-applications/agent-tools" className={styles.trendingLink}>Autonomous Agents</Link>
          </div>
        </div>
        
        <div className={styles.featuresGrid}>
          <div className={styles.featureCard}>
            <h3>Models & Infrastructure</h3>
            <p>Practical deployment guides for LLMs, embedding models, and hybrid RAG search architectures.</p>
          </div>
          
          <div className={styles.featureCard}>
            <h3>Agentic Ecosystem</h3>
            <p>Comprehensive comparisons of AI IDEs and autonomous closed-loop terminal agents.</p>
          </div>
          
          <div className={styles.featureCard}>
            <h3>Protocols & Tooling</h3>
            <p>Industry standards, Model Context Protocol (MCP), and workflow automation orchestrations.</p>
          </div>
        </div>
      </div>
    </main>
  )
}
