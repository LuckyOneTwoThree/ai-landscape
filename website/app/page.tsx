import styles from './page.module.css'
import Link from 'next/link'
import { getModules, getDocumentsInModule } from '@/lib/markdown'

export default function Home() {
  const modules = getModules('zh');
  let firstDocLink = '/docs';
  if (modules.length > 0) {
    const firstModule = modules[0];
    const docs = getDocumentsInModule(firstModule.id, 'zh');
    if (docs.length > 0) {
      firstDocLink = `/docs/${firstModule.id}/${docs[0].slug}`;
    }
  }

  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <div className={styles.heroSection}>
          <h1 className={styles.title}>
            AI Landscape
          </h1>
          
          <p className={styles.subtitle}>
            个人全栈开发者的 AI 生存指南。打破同质化，直击底层逻辑。
            从基础模型选型、基础设施部署，到全自主 Agent 构建的最佳实践。
          </p>
          
          <div className={styles.actionContainer}>
            <Link href={firstDocLink} className={styles.primaryBtn}>
              阅读文档
            </Link>
            <a href="https://github.com/LuckyOneTwoThree/ai-landscape" target="_blank" rel="noreferrer" className={styles.secondaryBtn}>
              GitHub 仓库
            </a>
          </div>

          <div className={styles.trendingSection}>
            <span className={styles.trendingLabel}>🔥 热门导览:</span>
            <Link href="/docs/01-foundation-models/llm" className={styles.trendingLink}>本地大模型</Link>
            <Link href="/docs/02-infrastructure/vector-db" className={styles.trendingLink}>向量检索与 RAG</Link>
            <Link href="/docs/10-applications/agent-tools" className={styles.trendingLink}>自主 Agent</Link>
          </div>
        </div>
        
        <div className={styles.featuresGrid}>
          <div className={styles.featureCard}>
            <h3>模型与基础设施</h3>
            <p>告别跑分党，深扒本地显卡算力边界，揭秘向量检索与混合架构的最优解。</p>
          </div>
          
          <div className={styles.featureCard}>
            <h3>Agent 生态演进</h3>
            <p>从 Cursor IDE 代码提效，到完全自主闭环的终端 Agent 实战与深度评测。</p>
          </div>
          
          <div className={styles.featureCard}>
            <h3>协议与工具链</h3>
            <p>拥抱 2026 行业标准，掌握 Model Context Protocol (MCP) 与工作流编排的组装魔法。</p>
          </div>
        </div>
      </div>
    </main>
  )
}
