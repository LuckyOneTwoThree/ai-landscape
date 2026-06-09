import { getModules, getDocumentsInModule, getDocumentContent } from '@/lib/markdown'
import styles from './markdown.module.css'
import Link from 'next/link'
import TableOfContents from '@/components/TableOfContents'

export async function generateStaticParams() {
  const modules = getModules()
  const paths = []
  
  for (const mod of modules) {
    const docs = getDocumentsInModule(mod.id)
    for (const doc of docs) {
      paths.push({
        moduleId: mod.id,
        slug: doc.slug,
      })
    }
  }
  
  return paths
}

type Params = Promise<{ moduleId: string, slug: string }>

export default async function DocumentPage({
  params
}: {
  params: Params
}) {
  const resolvedParams = await params;
  const { contentHtml, frontmatter } = await getDocumentContent(resolvedParams.moduleId, resolvedParams.slug)
  
  return (
    <div className={styles.pageContainer}>
      <article className={styles.markdownBody}>
        <div dangerouslySetInnerHTML={{ __html: contentHtml }} />
      </article>
      <aside className={styles.tocAside}>
        <TableOfContents locale="zh" />
      </aside>
    </div>
  )
}
